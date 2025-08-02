import datetime
import random

from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.csrf import csrf_exempt
from sslcommerz_python_api import SSLCSession

from carts.models import Cart, CartProduct
from carts.utils import get_session_key
from orders.utils import send_order_confirmation_email
from products.models import Product

from .models import Order, OrderProduct, Payment


def place_order(request):
    if request.user.is_authenticated:
        cart = get_object_or_404(Cart, user=request.user)
    else:
        cart = get_object_or_404(Cart, session_key=get_session_key())

    cart_products = CartProduct.objects.filter(cart=cart).select_related("product")

    if cart_products.count() == 0:
        return redirect("home")

    quantity = 0
    total = 0
    for cart_product in cart_products:
        total += cart_product.product.price * cart_product.quantity
        quantity += cart_product.quantity

    if request.method == "POST":
        payment_option = request.POST.get("payment_method")  # cash / sslcommercez

        try:
            current_date = datetime.date.today()
            order_number = current_date.strftime("%Y%m%d%H%M%S") + str(
                random.randint(1000, 9999)
            )
            # 202550510
            current_user = request.user

            order = Order.objects.create(
                user=current_user,
                mobile=current_user.mobile,
                address_line_1=current_user.address_line_1,
                address_line_2=current_user.address_line_2,
                country=current_user.country,
                postcode=current_user.postcode,
                city=current_user.city,
                order_note=request.POST.get("order_note", ""),
                order_total=total,
                status="Pending",
                order_number=order_number,
            )

            for cart_item in cart_products:
                OrderProduct.objects.create(
                    order=order,
                    product=cart_item.product,
                    quantity=cart_item.quantity,
                    product_price=cart_item.product.price,
                )

                product = Product.objects.get(id=cart_item.product.id)
                if product.stock >= cart_item.quantity:
                    product.stock -= cart_item.quantity
                    product.save()

            send_order_confirmation_email(current_user, order)

            if payment_option == "cash":
                cart_products.delete()
                return redirect("order_complete")
            elif payment_option == "sslcommerz":
                return redirect("payment")

        except Exception as e:
            return HttpResponse("Error occurred: " + str(e))

    context = {
        "total": total,
        "quantity": quantity,
        "cart_items": cart_products,
        "grand_total": total + settings.DELIVERY_CHARGE,
    }

    return render(request, "orders/checkout.html", context=context)


def payment(request):
    mypayment = SSLCSession(
        sslc_is_sandbox=settings.SSLCOMMERZ_IS_SANDBOX,
        sslc_store_id=settings.SSLCOMMERZ_STORE_ID,
        sslc_store_pass=settings.SSLCOMMERZ_STORE_PASS,
    )

    status_url = request.build_absolute_uri("payment_status")

    mypayment.set_urls(
        success_url=status_url,
        fail_url=status_url,
        cancel_url=status_url,
        ipn_url=status_url,
    )

    user = request.user
    order = Order.objects.filter(user=user, status="Pending").last()

    if not order:
        return HttpResponse("No pending order found.")

    # ✅ Fallbacks to prevent missing required fields
    address1 = order.address_line_1 or "Not Provided"
    address2 = order.address_line_2 or "N/A"
    city = order.city or "Dhaka"
    postcode = order.postcode or "0000"
    country = order.country or "Bangladesh"
    phone = order.mobile or "0000000000"
    email = user.email or "dummy@example.com"
    name = user.username or "Customer"
    shipping_to = user.first_name or "Customer"

    mypayment.set_product_integration(
        total_amount=order.order_total,
        currency="BDT",
        product_category="clothing",
        product_name="demo-product",
        num_of_item=2,
        shipping_method="YES",
        product_profile="None",
    )

    mypayment.set_customer_info(
        name=name,
        email=email,
        address1=address1,  # Required field: cus_add1
        address2=address2,
        city=city,
        postcode=postcode,
        country=country,
        phone=phone,
    )

    mypayment.set_shipping_info(
        shipping_to=shipping_to,
        address=address2,
        city=city,
        postcode=postcode,
        country=country,
    )

    response_data = mypayment.init_payment()
    print("SSLCOMMERZ Response:", response_data)  # For debugging

    if response_data.get("status") == "FAILED":
        order.status = "Failed"
        order.save()
        reason = response_data.get("failedreason", "Unknown error occurred.")
        return HttpResponse(f"SSLCommerz payment initiation failed: {reason}")

    gateway_url = response_data.get("GatewayPageURL")
    if not gateway_url:
        return HttpResponse(
            f"GatewayPageURL not returned. Full response: {response_data}"
        )

    return redirect(gateway_url)


@csrf_exempt
def payment_status(request):
    if request.method == "POST":
        payment_data = request.POST
        if payment_data["status"] == "VALID":
            val_id = payment_data["val_id"]
            tran_id = payment_data["tran_id"]

            order = Order.objects.filter(user=request.user).last()

            payment = Payment.objects.create(
                user=request.user,
                payment_id=val_id,
                payment_method="SSLCommerz",
                amount_paid=order.order_total,
                status="Completed",
            )

            order.status = "Completed"
            order.payment = payment
            order.save()

            # CartItems will be automatically deleted
            Cart.objects.filter(user=request.user).delete()

            context = {
                "order": order,
                "transaction_id": tran_id,
            }
            return render(request, "orders/order-success.html", context)

        else:
            return render(request, "orders/payment-failed.html")

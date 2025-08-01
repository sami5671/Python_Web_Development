from django.core.paginator import Paginator
from django.db.models import Count
from django.shortcuts import get_object_or_404, redirect, render

from .models import Category, Product, Review

# Create your views here.


def home(request):
    categories = Category.objects.annotate(product_count=Count("products"))
    context = {"categories": categories}
    return render(request, "products/home.html", context=context)


def category_products(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)

    products = Product.objects.filter(category=category)

    paginator = Paginator(products, 6)
    page = request.GET.get("page")
    paged_products = paginator.get_page(page)

    context = {
        "products": paged_products,
        "category": category,
    }
    return render(request, "products/category_products.html", context)


def product_detail(request, product_slug):
    product = get_object_or_404(Product, slug=product_slug)

    context = {
        "product": product,
        "rating_counts": 0,
        "rating_percentages": 0,
        "reviews": 0,
    }
    return render(request, "products/product-left-thumbnail.html", context)

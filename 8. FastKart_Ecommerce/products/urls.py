from django.urls import include, path

from . import views

urlpatterns = [
    path("", views.home),
    path(
        "categories/<slug:category_slug>/products",
        views.category_products,
        name="category_products",
    ),
    path("products/<slug:product_slug>", views.product_detail, name="product_detail"),
]

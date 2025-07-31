from django.db.models import Count
from django.shortcuts import render

from .models import Category, Product, Review

# Create your views here.


def home(request):
    categories = Category.objects.annotate(product_count=Count("products"))
    context = {"categories": categories}
    return render(request, "products/home.html", context=context)

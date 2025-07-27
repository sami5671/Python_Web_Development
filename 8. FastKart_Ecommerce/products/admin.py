from django.contrib import admin
from django.utils.html import format_html

from .models import Category, Product, ProductImage, Review

admin.site.register([Category, Product, ProductImage, Review])

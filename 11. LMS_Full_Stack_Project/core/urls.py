from django.urls import path

from .views import category_list_create

urlpatterns = [path("categories/", category_list_create, name="category_list_create")]

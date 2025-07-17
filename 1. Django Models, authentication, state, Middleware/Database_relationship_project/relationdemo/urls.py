from django.urls import path

from . import views

urlpatterns = [
    path("one-to-one/", views.demo_one_to_one, name="one-to-one"),
    path("user/<int:pk>", views.user, name="user"),
    path("one-to-many/", views.demo_one_to_many, name="one-to-many"),
    path("many-to-many/", views.demo_many_to_many, name="many-to-many"),
    path(
        "book_name/<str:book_title>/", views.get_book_details, name="get_book_details"
    ),
    path(
        "author/<str:author_name>/", views.get_author_details, name="get_author_details"
    ),
    path("book/<int:book_id>/", views.get_book_by_id, name="get_book_by_id"),
]

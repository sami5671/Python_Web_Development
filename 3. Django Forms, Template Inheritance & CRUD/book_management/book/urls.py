from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="book_list"),
    path("create/", views.addNewBook, name="add_book"),
    path("update/<int:id>/", views.updateBookInfo, name="book_update"),
    path("delete/<int:id>/", views.deleteBookInfo, name="book_delete"),
]

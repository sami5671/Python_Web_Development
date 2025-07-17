from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
    # path("home/", views.home, name="home"), #function based
    path("home/", views.StudentLists.as_view(), name="home"),  # class based
    # path("create/", views.create_student, name="create_student"),  # function based
    path(
        "create/", views.createStudent.as_view(), name="create_student"
    ),  # function based
    # path("edit/<int:id>/", views.update_student, name="update_student"),# function based
    path(
        "edit/<int:id>/", views.UpdateStudentData.as_view(), name="update_student"
    ),  # class based
    # path("delete/<int:id>/", views.delete_student, name="delete_student"),  # function based
    path(
        "delete/<int:id>/", views.DeleteStudent.as_view(), name="delete_student"
    ),  # class based
]

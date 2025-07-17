from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include, path

from . import views

urlpatterns = [
    path("", views.task_list, name="task_list"),
    path("task/<int:task_id>", views.task_detail, name="task_detail"),
    path("task/<int:task_id>/delete/", views.task_delete, name="task_delete"),
    path(
        "task/<int:task_id>/mark_completed/",
        views.task_mark_completed,
        name="task_mark_completed",
    ),
    path("register/", views.register, name="register"),
    path("login/", auth_views.LoginView.as_view(template_name=""), name="login"),
    path("logout/", auth_views.LoginView.as_view(), name="logout"),
]

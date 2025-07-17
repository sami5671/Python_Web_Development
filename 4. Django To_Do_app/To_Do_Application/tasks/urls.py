from django.urls import path

from .views import (
    home,
    register,
    task_create,
    task_delete,
    task_detail,
    user_login,
    user_logout,
)

urlpatterns = [
    # Authentication
    path("register/", register, name="register"),
    path("login/", user_login, name="login"),
    path("logout/", user_logout, name="logout"),
    # Tasks
    path("", home, name="home"),
    path("tasks/<int:task_id>/", task_detail, name="task_detail"),
    path("delete/<int:task_id>/", task_delete, name="delete"),
    path("create/", task_create, name="create"),
]

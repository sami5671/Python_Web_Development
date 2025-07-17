from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("secure/", views.secure, name="secure"),
    path("secure-class/", views.SecureClassView.as_view(), name="secure-class"),
    path("register/", views.register, name="register"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
]

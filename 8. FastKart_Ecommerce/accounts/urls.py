from django.urls import path

from . import views

urlpatterns = [
    path("signup/", views.user_signup, name="signup"),
    path("verify/<uidb64>/<token>/", views.verify_email, name="verify-email"),
    path("login/", views.user_login, name="login"),
    path("logout/", views.user_logout, name="logout"),
]

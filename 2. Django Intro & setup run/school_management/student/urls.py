from django.urls import path

from . import views

urlpatterns = [
    path("profile/", views.profile, name="student_profile"),
    path("home/", views.home, name="student_home"),
]

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from .decorators import admin_required, editor_required, author_required

# *fGzhp83v*cE#bY!


# Create your views here.
def home(request):
    return render(request, "home.html")


def unauthorized(request):
    return HttpResponse("You are not authorized to view this page.")


# @login_required
# def admin(request):
#     user = request.user
#     if user.is_superuser:
#         return render(request, "admin.html")
#     else:
#         return HttpResponse("You are not authorized to view this page.")


# @login_required
# def editor(request):
#     user = request.user
#     if user.is_superuser or user.groups.filter(name="editor").exists():
#         return render(request, "editor.html")
#     else:
#         return HttpResponse("You are not authorized to view this page.")


# @login_required
# def author(request):
#     user = request.user
#     if (
#         user.is_superuser
#         or user.groups.filter(name="editor").exists()
#         or user.groups.filter(name="author").exists()
#     ):
#         return render(request, "author.html")
#     else:
#         return HttpResponse("You are not authorized to view this page.")


@admin_required
def admin(request):
    return render(request, "admin.html")


@editor_required
def editor(request):
    return render(request, "editor.html")


@author_required
def author(request):
    return render(request, "author.html")


# from django.contrib.auth.models import Group

# # Create a new group named "admin" if it does not exist
# group, created = Group.objects.get_or_create(name="editor")

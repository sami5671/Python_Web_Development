from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.db import models
from django.shortcuts import redirect, render

from .forms import TodoForm
from .models import Task

# Abstract User
# Abstract Base User

# Groups


# Register View
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("/")
    else:
        form = UserCreationForm()
    return render(request, "register.html", {"form": form})


# Login View
def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("/")
    else:
        form = AuthenticationForm()
    return render(request, "login.html", {"form": form})


# Logout View
@login_required
def user_logout(request):
    logout(request)
    return redirect("login")


# Home View
@login_required
def home(request):
    tasks = Task.objects.filter(created_by=request.user)

    status = request.GET.get("status")
    if status == "completed":
        tasks = tasks.filter(is_completed=True)
    elif status == "remaining":
        tasks = tasks.filter(is_completed=False)

    search = request.GET.get("ghorardim")
    if search:
        tasks = tasks.filter(
            models.Q(title__icontains=search) | models.Q(description__icontains=search),
        )

    return render(request, "index.html", {"tasks": tasks, "search": search})


@login_required
def task_detail(request, task_id):
    task = Task.objects.get(pk=task_id, created_by=request.user)
    return render(request, "task_detail.html", {"task": task})


@login_required
def task_delete(request, task_id):
    task = Task.objects.get(pk=task_id, created_by=request.user)
    task.delete()
    return redirect("/")


@login_required
def task_create(request):
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            # form.instance.created_by = request.user
            task = form.save(commit=False)
            task.created_by = request.user
            task.save()
            return redirect("/")
    else:
        form = TodoForm()
    return render(request, "create_todo.html", {"form": form})

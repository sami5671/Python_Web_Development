from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from . import forms, models
from .forms import StudentForm

# Create your views here.

# 1. HTML form
# 2. Form Api
# 3. Model Form


# def home(request):
# print(request.POST)
# this for HTML form
# if request.method == "POST":
#     name = request.POST.get("name")
#     email = request.POST.get("email")
#     phone = request.POST.get("phone")
#     password = request.POST.get("password")
#     checkbox = request.POST.get("checkbox")
#     photo = request.FILES.get("photo")

#     if checkbox == "on":
#         checkbox = True
#     else:
#         checkbox = False

#     student = models.Student(
#         name=name,
#         email=email,
#         phone=phone,
#         password=password,
#         checkbox=checkbox,
#         photo=photo,
#     )  # student class er akta object
#     student.save()
#     return render(request, "student/index.html")
# else:
#     return render(request, "student/index.html")

# this for model form


# For function based views
def home(request):
    students = models.Student.objects.all()
    return render(request, "student/index.html", {"students": students})


# For Class based views
class StudentLists(ListView):
    model = models.Student
    template_name = "student/index.html"
    context_object_name = "students"


#  For function based views
@login_required
def create_student(request):
    if request.method == "POST":
        form = forms.StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = forms.StudentForm()
    return render(request, "student/create_student.html", {"form": form})


# for class based view
class createStudent(LoginRequiredMixin, CreateView):
    form_class = forms.StudentForm
    template_name = "student/create_student.html"
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        student = form.save(
            commit=False
        )  # database e data save hobe na but user er submit kora data peye jabo
        student.user = self.request.user
        student.save()
        return super().form_valid(form)


def update_student(request, id):
    student = models.Student.objects.get(id=id)
    form = forms.StudentForm(instance=student)

    if request.method == "POST":
        form = forms.StudentForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            return redirect("home")
    return render(request, "student/edit_student.html", {"form": form, "edit": True})


# For Class based views
class UpdateStudentData(LoginRequiredMixin, UpdateView):
    form_class = forms.StudentForm
    model = models.Student
    template_name = "student/edit_student.html"
    success_url = reverse_lazy("home")
    pk_url_kwarg = "id"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["edit"] = True
        return context


def delete_student(request, id):
    student = models.Student.objects.get(id=id)
    student.delete()
    return redirect("home")


# For Class based views
class DeleteStudent(LoginRequiredMixin, DeleteView):
    model = models.Student
    pk_url_kwarg = "id"
    success_url = reverse_lazy("home")
    template_name = "student/delete_student.html"

    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)


def signUp(request):
    if request.method == "POST":
        form = forms.SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = forms.SignUpForm()

    return render(request, "student/auth_form.html", {"form": form})


def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect("home")

    else:
        form = AuthenticationForm()
    return render(request, "student/auth_form.html", {"form": form})


def user_logout(request):
    logout(request)
    return redirect("home")


@login_required
def profile(request):
    students = models.Student.objects.filter(user=request.user)
    print(students)
    return render(request, "student/profile.html", {"students": students})

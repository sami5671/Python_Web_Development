from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


def home(request):

    # request.user.userprofile

    if request.user.is_authenticated:
        lalala = "lalala"

    return render(request, "home.html")


@login_required
def secure(request):

    user = request.user

    # blog.created_by = user

    # if blog.created_by == request.user:
    #     delete()

    # else:
    #     return HTTPResponseForbidden()

    # blog.objects.filter(created_by=request.user)

    return render(request, "secure.html")


class SecureClassView(LoginRequiredMixin, TemplateView):
    template_name = "secure.html"


from django import forms


class RegisterForm(UserCreationForm):
    habijabi = forms.CharField()

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2", "habijabi"]
        widgets = {
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "username": forms.TextInput(attrs={"class": "form-control"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields["username"].widget.attrs.update({"class": "form-control"})
        self.fields["password1"].widget.attrs.update({"class": "form-control"})
        self.fields["password2"].widget.attrs.update({"class": "form-control"})

        self.fields["password1"].help_text = None


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = RegisterForm()

    context = {
        "form": form,
    }
    return render(request, "register.html", context)


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()  # authenticate function
            login(request, user)
            return redirect("home")
    else:
        form = AuthenticationForm()

    context = {
        "form": form,
    }
    return render(request, "login.html", context)


def logout_view(request):

    logout(request)

    return redirect("home")

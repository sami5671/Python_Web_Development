from django import forms

from . import models


class StudentForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = models.Student
        fields = "__all__"
        labels = {"name": "Full Name", "photo": "Upload Photo"}
        help_texts = {"email": "Email will be confidential"}

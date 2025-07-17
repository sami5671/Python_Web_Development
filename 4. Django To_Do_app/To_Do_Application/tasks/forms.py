from django import forms

from .models import Task


class TodoForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["title", "description", "due_date", "due_time", "is_completed"]

        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "description": forms.Textarea(attrs={"class": "form-control"}),
            "due_date": forms.DateInput(
                attrs={"type": "date", "class": "form-control"}
            ),
            "due_time": forms.TimeInput(
                attrs={"type": "time", "class": "form-control"}
            ),
        }

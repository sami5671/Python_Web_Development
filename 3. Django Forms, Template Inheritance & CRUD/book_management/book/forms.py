from django import forms

from .models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["title", "authorName", "price", "description"]
        widgets = {
            "title": forms.TextInput(
                attrs={
                    "class": "w-full p-2 border rounded",
                    "Placeholder": "Enter the title of the book",
                }
            ),
            "authorName": forms.TextInput(
                attrs={
                    "class": "w-full p-2 border rounded",
                    "Placeholder": "Enter the Author name of the book",
                }
            ),
            "price": forms.TextInput(
                attrs={
                    "class": "w-full p-2 border rounded",
                    "Placeholder": "Enter the Price",
                }
            ),
            "description": forms.Textarea(
                attrs={
                    "class": "w-full p-2 border rounded",
                    "Placeholder": "Enter the description here .....",
                    "rows": 7,
                }
            ),
        }

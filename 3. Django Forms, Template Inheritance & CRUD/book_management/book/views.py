from django.shortcuts import redirect, render

from .forms import BookForm
from .models import Book


# Create your views here.
def home(request):
    books = Book.objects.all()
    context = {"books": books}
    return render(request, "home.html", context)


def addNewBook(request):
    if request.method == "POST":
        book_form = BookForm(request.POST)
        if book_form.is_valid():
            book_form.save()
            return redirect("/")
    else:
        book_form = BookForm()

    context = {"form": book_form}
    return render(request, "book_form.html", context)


def updateBookInfo(request, id):
    book = Book.objects.get(id=id)

    if request.method == "POST":
        book_form = BookForm(request.POST, instance=book)
        if book_form.is_valid():
            book_form.save()
            return redirect("/")
    else:
        book_form = BookForm(instance=book)

    context = {"form": book_form}
    return render(request, "book_form.html", context)


def deleteBookInfo(request, id):
    book = Book.objects.get(id=id)
    book.delete()
    return redirect("/")

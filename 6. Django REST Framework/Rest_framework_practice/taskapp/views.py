from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Task, Contact, Author, Book
from .serializers import (
    TaskSerializer,
    ContactSerializer,
    AuthorSerializer,
    BookSerializer,
)
from rest_framework.decorators import action
from rest_framework.response import Response


class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    @action(detail=False, methods=["get"])
    def say_hello(self, request):
        return Response({"message": "Hello, World!"})


class ContactViewSet(ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

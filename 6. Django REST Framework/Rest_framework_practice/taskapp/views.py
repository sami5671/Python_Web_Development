from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Author, Book, Contact, Task
from .serializers import (
    AuthorSerializer,
    BookSerializer,
    ContactSerializer,
    TaskSerializer,
)


class TaskPagination(PageNumberPagination):
    page_size = 2


class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    pagination_class = TaskPagination
    # permission_classes = [AllowAny]
    permission_classes = [IsAuthenticated]

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ["completed"]
    search_fields = ["title", "description"]
    ordering_fields = ["id", "title", "completed", "created_at"]

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)

    # automatically take the user
    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)

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

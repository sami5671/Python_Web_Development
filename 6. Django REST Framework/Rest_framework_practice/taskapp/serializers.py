from rest_framework import serializers
from .models import Task, Contact, Author, Book


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"  # Include all fields
        # fields = [
        #     "id",
        #     "title",
        #     "description",
        #     "completed",
        #     "created_at",
        # ]  # Exclude 'user'
        # read_only_fields = ["id", "created_at"]


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = "__all__"
        extra_kwargs = {
            "name": {
                "required": True,
                "min_length": 3,
                "error_messages": {
                    "min_length": "নাম কমপক্ষে ৩ অক্ষর হতে হবে।",
                },
            },
        }


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"


class BookSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(
        queryset=Author.objects.all()
    )  # Dropdown for authors

    class Meta:
        model = Book
        fields = "__all__"

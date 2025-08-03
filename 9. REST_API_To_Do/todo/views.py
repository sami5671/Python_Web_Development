from django.shortcuts import render
from django.http import HttpResponse

from django.views import View
from django.views.decorators.csrf import csrf_exempt

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Todo

import json


def todo_list(request):

    if request.method == "POST":
        # Handle the form submission here
        return HttpResponse("Form submitted successfully.")

    else:

        return HttpResponse("This is the todo list page.")


# View namok class hocche boss
class TodoListView(View):
    def get(self, request):
        todos = Todo.objects.all()
        context = {
            "todos": todos,
        }
        return render(request, "todo_list.html", context)

    def post(self, request):
        return HttpResponse("Form submitted successfully.")


# class TodoListApiView(View):
#     def get(self, request):
#         todos = Todo.objects.all()

#         formatted_todo = []

#         for todo in todos:
#             formatted_todo.append(
#                 {
#                     "id": todo.id,
#                     "title": todo.title,
#                     "description": todo.description,
#                     "completed": todo.completed,
#                     "created_at": todo.created_at.strftime("%d/%m/%Y, %H:%M:%S"),
#                     "updated_at": todo.updated_at.strftime("%d/%m/%Y, %H:%M:%S"),
#                 }
#             )

#         formatted_todo = json.dumps(formatted_todo)

#         return HttpResponse(formatted_todo, content_type="application/json")

#     def post(self, request):
#         formatted_data = json.loads(request.body)

#         created_todo = Todo.objects.create(
#             title=formatted_data["title"],
#             description=formatted_data["description"],
#         )

#         data_to_return = {
#             "id": created_todo.id,
#             "title": created_todo.title,
#             "description": created_todo.description,
#         }

#         data_to_return = json.dumps(data_to_return)

#         return HttpResponse(data_to_return, content_type="application/json")


from rest_framework.serializers import ModelSerializer


class TodoSerializer(ModelSerializer):
    class Meta:
        model = Todo
        fields = ["id", "title", "description", "completed", "created_at", "updated_at"]


from rest_framework.permissions import IsAdminUser


class TodoListApiView(APIView):

    # By which class can user authenticate
    authentication_classes = []

    # By which class can user authorize
    permission_classes = []

    def get(self, request):
        todos = Todo.objects.all()
        formatted_todo = TodoSerializer(todos, many=True).data
        return Response(formatted_todo)

    def post(self, request):
        formatted_data = request.data

        serializer = TodoSerializer(data=formatted_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors)


from rest_framework.generics import ListCreateAPIView


class TodoListApiView2(ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class TodoDetailApiView(APIView):
    def get(self, request, pk):
        todo = Todo.objects.get(pk=pk)
        formatted_todo = TodoSerializer(todo).data
        return Response(formatted_todo)

    def put(self, request, pk):
        todo = Todo.objects.get(pk=pk)
        formatted_data = request.data

        serializer = TodoSerializer(instance=todo, data=formatted_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors)

    def delete(self, request, pk):
        todo = Todo.objects.get(pk=pk)
        todo.delete()
        return Response({"message": "Todo deleted successfully."})


from rest_framework.generics import RetrieveAPIView, UpdateAPIView, DestroyAPIView

from rest_framework.generics import RetrieveUpdateDestroyAPIView


class TodoDetailApiView2(RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


# issues
# 1. Shob custom korte hocche (convert) ✅
# 2. For loop chalay list banay then kaj korte hocche ✅
# 3. JSON string e convert korte hocche ✅
# 4. We have to set content type manually ✅
# 5. CSRF Issue ✅
# 6. Format data on receive ✅
# 7. Create data manually ✅


# Auto Documentation
# Swagger

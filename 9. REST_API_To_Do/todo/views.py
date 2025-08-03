import json

from django.shortcuts import HttpResponse, render
from django.views import View

from .models import Todo


# Create your views here.
def todo_list(request):
    return HttpResponse("simple todo list")


class TodoListView(View):
    def get(self, request):
        todos = Todo.objects.all()
        context = {"todos": todos}
        return render(request, "todo_list.html", context)

    def post(self, request):
        return HttpResponse("simple todo list")


class TodoListApiView(View):
    def get(self, request):
        todos = Todo.objects.all()

        formatted_todo = []

        for todo in todos:
            formatted_todo.append(
                {
                    "id": todo.id,
                    "title": todo.title,
                    "description": todo.description,
                    "completed": todo.completed,
                    "created_at": todo.created_at.strftime("%d/%m/%Y, %H:%M:%S"),
                    "updated_at": todo.updated_at.strftime("%d/%m/%Y, %H:%M:%S"),
                }
            )

        formatted_todo = json.dumps(formatted_todo)

        return HttpResponse(formatted_todo, content_type="application/json")

    def post(self, request):
        formatted_data = json.loads(request.body)

        created_todo = Todo.objects.create(
            title=formatted_data["title"],
            description=formatted_data["description"],
        )

        data_to_return = {
            "id": created_todo.id,
            "title": created_todo.title,
            "description": created_todo.description,
        }

        data_to_return = json.dumps(data_to_return)

        return HttpResponse(data_to_return, content_type="application/json")

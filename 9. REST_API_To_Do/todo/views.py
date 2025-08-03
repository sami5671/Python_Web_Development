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
        print(formatted_data)

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


# issues
# 1. Shob custom korte hocche (convert) ✅
# 2. For loop chalay list banay then kaj korte hocche ✅
# 3. JSON string e convert korte hocche ✅
# 4. We have to set content type manually ✅
# 5. CSRF Issue ✅
# 6. Format data on receive ✅
# 7. Create data manually ✅

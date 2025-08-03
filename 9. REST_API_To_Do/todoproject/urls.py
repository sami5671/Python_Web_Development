from django.contrib import admin
from django.urls import path, include

from todo.views import (
    todo_list,
    TodoListView,
    TodoListApiView,
    TodoListApiView2,
    TodoDetailApiView,
    TodoDetailApiView2,
)


V1_URLS = [
    path("todos/", TodoListApiView2.as_view(), name="todo_list_api"),
    path("todos/<str:pk>/", TodoDetailApiView2.as_view(), name="todo_list_api_detail"),
]

# V2_URLS = [...]

API_URLS = [
    path("v1/", include(V1_URLS)),
    # path("v2/", include(V2_URLS)),
]

urlpatterns = [
    path("admin/", admin.site.urls),
    path("todos/", TodoListView.as_view(), name="todo_list"),
    path("api/", include(API_URLS)),
]

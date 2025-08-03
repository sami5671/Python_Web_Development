from django.shortcuts import HttpResponse, render


# Create your views here.
def todo_list(request):
    return HttpResponse("simple todo list")

from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def profile(request):
    user_data = {
        "name": "SAMI ALAM",
        "email": "samialam@gmail.com",
        "age": 10,
        "district": "dhaka",
    }
    # return HttpResponse("<h1>Student profile</h1>")
    return render(request, "student/index.html", user_data)


def home(request):
    return HttpResponse("<h1>Student Home</h1>")

from django.http import HttpResponse
from django.shortcuts import render

from .models import Post


# Create your views here.
def home(request):
    # get all data
    posts = Post.objects.all()
    # result = ""
    # for post in posts:
    #     result += f"{post.title} - {post.content} <br>"
    # return HttpResponse(result)
    return render(request, "post_list.html")

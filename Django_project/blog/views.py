from django.shortcuts import render
from django.http import HttpResponse, request
from datetime import datetime
from .models import Post
posts = [
    {
        'author': "Thanh La",
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': datetime.now
    },
    {
        'author': "Thanh DepTrai",
        'title': 'Blog Post 2',
        'content': 'First post content',
        'date_posted': datetime.now
    }

]
def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html')
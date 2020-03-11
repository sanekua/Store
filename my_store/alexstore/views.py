from django.shortcuts import render
from django.http import HttpResponse
from .models import Post


def about(request):
    return render(request, 'alexstore/about.html',{'title': 'What a beautiful day'})


def home(request):
    context = {
        'posts' : Post.objects.all(),
        #'posts' : posts,
        'title':'Our tite'
    }
    return render(request, 'alexstore/home.html',context)

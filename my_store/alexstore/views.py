from django.shortcuts import render
from django.http import HttpResponse


posts = [
    {
        'author': 'Alex',
        'titlee' : 'Blog post',
        'content' : 'our post content',
        'date' : ' 24 Febr',

    },
    {
        'author': 'Max',
        'titlee': 'Blog post 2',
        'content': 'content 2',
        'date': ' 24 February day number 2',

    }


]


def about(request):
    return render(request, 'alexstore/about.html')



def home(request):
    context = {
        'posts' : posts
    }
    return render(request, 'alexstore/home.html',context)

# Create your views here.

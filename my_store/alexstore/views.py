from django.shortcuts import render
from django.http import HttpResponse



def index(request):
    return HttpResponse("<h3>  Helllo world </h3>")

# Create your views here.

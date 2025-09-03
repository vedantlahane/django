from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse("Hello, welcome to the blog index!")


def hello_name(request, name):
    return HttpResponse(f"Hello, {name}!")
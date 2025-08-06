from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def hello(request):
    return HttpResponse("Hello, world! This is the Little Lemon restaurant app.")
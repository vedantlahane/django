from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def hello(request):
    return HttpResponse("Hello, world! This is the Little Lemon restaurant app.")


def jsonResonse(request):
    data = {
        "name": "Little Lemon",
        "location": "Chicago",
        "cuisine": "Mediterranean",
        "rating": 4.5,
        "open_hours": {
            "Monday": "10:00 AM - 10:00 PM",
            "Tuesday": "10:00 AM - 10:00 PM",
            "Wednesday": "10:00 AM - 10:00 PM",
            "Thursday": "10:00 AM - 10:00 PM",
            "Friday": "10:00 AM - 11:00 PM",
            "Saturday": "9:00 AM - 11:00 PM",
            "Sunday": "9:00 AM - 9:00 PM"
        }
    }
    return HttpResponse(data , content_type="application/json")


def datafile(requesr, name):
    return HttpResponse("Hello User, this is the data file for " + name + ".")
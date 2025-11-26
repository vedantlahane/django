from django.http import HttpResponse

def home_view(request):
    return HttpResponse("Hello from Function-Based View!")

from django.views import View

class AboutView(View):
    def get(self, request):
        return HttpResponse("Hello from Class-Based View!")

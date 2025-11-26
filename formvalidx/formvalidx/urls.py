from django.contrib import admin
from django.urls import path
from accounts.views import validate_code

urlpatterns = [
    path('admin/', admin.site.urls),
    path('validate/', validate_code),
]

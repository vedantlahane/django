from django.contrib import admin
from django.urls import path
from weather.views import weather_dashboard

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', weather_dashboard, name='weather_dashboard'),
]

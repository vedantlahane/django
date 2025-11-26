from django.contrib import admin
from django.urls import path
from main.views import home_view, AboutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home_view, name='home'),
    path('about/', AboutView.as_view(), name='about'),
]

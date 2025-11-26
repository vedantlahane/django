from django.contrib import admin
from django.urls import path
from feedback.views import submit_feedback, thank_you
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('feedback/', submit_feedback, name='submit_feedback'),
    path('thank-you/', thank_you, name='thank_you'),
]

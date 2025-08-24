from django.urls import path
from . import views

urlpatterns =[
    path('profile/<str:username>/', views.profile),
    path('users/', views.user_list, name='user_list'),
    path('about/', views.about, name='about'),
]
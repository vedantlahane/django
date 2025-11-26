from django.contrib import admin
from django.urls import path
from users.views import user_login, user_logout, dashboard, set_preference

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('dashboard/', dashboard, name='dashboard'),
    path('set-preference/', set_preference, name='set_preference'),
]

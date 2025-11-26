from django.contrib import admin
from django.urls import path
from accounts.views import user_login, user_logout, dashboard, forgot_password

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('dashboard/', dashboard, name='dashboard'),
    path('forgot-password/', forgot_password, name='forgot_password'),
]

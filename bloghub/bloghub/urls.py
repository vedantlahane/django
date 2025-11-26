
from django.contrib import admin
from django.urls import path
from posts.views import post_details

urlpatterns = [
    path('admin/', admin.site.urls),
    path('post/<int:post_id>',post_details,name="post"),
]

from django.contrib import admin
from django.urls import path
from shop.views import ingredient_list, search_ingredients

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ingredient_list, name='ingredient_list'),
    path('search/', search_ingredients, name='search_ingredients'),
]

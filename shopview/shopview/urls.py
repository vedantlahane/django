from django.contrib import admin
from django.urls import path
from products.views import product_list, product_detail, set_bg_color

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', product_list, name='product_list'),
    path('product/<int:pk>/', product_detail, name='product_detail'),
    path('set-bg-color/', set_bg_color, name='set_bg_color'),
]

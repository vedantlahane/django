from django.contrib import admin
from django.urls import path
from plants.views import home, plant_detail,choose_color

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('plant/<int:plant_id>/', plant_detail, name='plant_detail'),
    path('choose-color/', choose_color, name='choose_color'),

]

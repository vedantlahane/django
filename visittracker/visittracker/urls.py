from django.contrib import admin
from django.urls import path
from counter.views import visit_counter, reset_counter

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', visit_counter, name="visit_counter"),
    path('reset/', reset_counter, name="reset_counter"),
]

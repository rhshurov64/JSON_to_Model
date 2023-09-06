
from django.urls import path, include
from .views import *

urlpatterns = [
    path('home/', show_data, name = "home"),
    path('', show_data),
    path('delete/<int:id>/', delete_data, name="delete"),
    path('update/<int:id>/', update_data, name="update")
   
]
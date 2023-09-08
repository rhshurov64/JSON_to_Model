
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', show_data),
    path('home/', show_data, name = "home"),
    path('delete/<int:id>/', delete_data, name="delete"),
    path('update/<int:id>/', update_data, name="update"),
    path('select_chart/', chart_view, name="chart_view"),
    path('line_chart_view/', line_chart_view, name="line_chart_view"),
    path('bar_chart_view/', bar_chart_view, name="bar_chart_view"),
   
]
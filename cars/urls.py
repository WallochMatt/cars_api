from django.urls import path
from . import views

urlpatterns = [
    path('', views.cars_list),
    path('<int:pk>/', views.car_detail),
    path('<str:color>/', views.cars_by_color),
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.dealership_list),
    path('<int:pk>/', views.dealer_detail),
]
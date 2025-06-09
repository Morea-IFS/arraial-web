
from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.index, name="dress_dashboard"),
    path('api/getStatus/<int:pk>/', views.getEffect, name="dress_status"),  
]
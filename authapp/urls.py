from django.urls import path 
from authapp import views

urlpatterns = [
    path('user_creation_view/', views.user_creation_view),
]
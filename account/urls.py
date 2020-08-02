from django.urls import path, include
from . import views

urlpatterns = [
    path('auth/', views.auth, name='auth'),
    path('register/', views.register, name='register'),
]
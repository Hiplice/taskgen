from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.settings, name='settings'),
    path('auth/', views.auth, name='auth'),
    path('register/', views.register, name='register'),
]
from django.urls import path, include
from . import views

urlpatterns = [
    path('patterns/', views.patterns, name='patterns'),
    path('start/', views.start_test, name='start test'),
]
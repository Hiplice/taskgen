from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.show_tests, name='show tests'),
    path('pass/', views.start_test, name='show tests'),
]
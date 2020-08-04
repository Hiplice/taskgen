from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.show_tests, name='show tests'),
    path('start/', views.start_test, name='start test'),
]
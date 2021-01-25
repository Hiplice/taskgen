from django.urls import path, include, re_path
from . import views

urlpatterns = [
    path('', views.show_tests, name='show tests'),
    re_path(r'(?P<test_number>\d+)/', views.start_test, name='start test'),
    path('add', views.add_test, name='add test')
]
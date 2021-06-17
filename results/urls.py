from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.show_subjects, name='show tests'),
    path('topics/', views.show_topics, name='show topics'),
    path('results/', views.show_results, name='show results'),
]

from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.show_subjects, name='show tests'),
    path('topics/', views.show_topics, name='show topics'),
    path('topics/groups/', views.show_groups, name='show groups'),
    path('topics/groups/res/', views.show_res, name='show res'),
    path('results/', views.show_results, name='show results'),
    path('add/', views.add_subject, name='add subj'),
    path('remove/', views.remove_subject, name='remove subj'),
    path('topics/add/', views.add_topic, name='add topic'),
    path('topics/remove/', views.remove_topic, name='remove topic'),
    ]

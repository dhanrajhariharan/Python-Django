from django.urls import path
from . import views

urlpatterns = [
    path('create-user/', views.create_user, name='create_user'),
    path('create-task/', views.create_task, name='create_task'),
    path('task-report/', views.task_report, name='task_report'),
    
   
]

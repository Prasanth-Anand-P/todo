from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('task_update/<str:pk>/', views.taskUpdate, name = 'task_update'),
    path('task_delete/<str:pk>/', views.taskDelete, name = 'task_delete'),
    

]
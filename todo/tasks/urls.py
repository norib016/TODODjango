from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="list"),
    path('update_task/<str:pk>/', views.updateTask, name="update_task"),  ##Linking the path to update a task with update_task template
    path('delete/<str:pk>/', views.deleteTask, name="delete"),            ##Linking the path to delete a task with delete_task template

]

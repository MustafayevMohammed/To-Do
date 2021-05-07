from django.contrib import admin
from django.urls import path
from . import views
app_name = "tasks"

urlpatterns = [
    path("",views.index,name="index"),
    path("updatetask/<str:id>/",views.updateTask,name="update_task"),
    path("delete_task<str:id>/",views.deleteTask,name="delete_task"),
    path("completed",views.complededTasks,name="completed_tasks"),
]
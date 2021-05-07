from django.shortcuts import render,redirect
from . import models
from .forms import *
# Create your views here.

def index(request):
    tasks = models.Task.objects.filter(confirm="False")
    form = TaskForm()
    
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect("/")
    context = {
        "tasks":tasks,
        "form":form,
    }
    return render(request,"index.html",context)


def updateTask(request,id):
    task = models.Task.objects.get(id=id)
    form = TaskForm(instance=task)

    if request.method == "POST":
        form = TaskForm(request.POST,instance=task)
        if form.is_valid:
            form.save()
            return redirect("/")

    context = {
        "form":form,
    }
    return render(request,"update_task.html",context)

def deleteTask(request,id):
    task = models.Task.objects.get(id=id)

    task.delete()
    return redirect("/")
    context = {
        "task":task,
    }
    return render(request,"delete_task.html",context)

def complededTasks(request):
    tasks = models.Task.objects.filter(confirm="True")
    
    context = {
        "tasks":tasks,
    }

    return render(request,"completeds.html",context)
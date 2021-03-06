from django.shortcuts import render,redirect
from . import models
from .forms import *
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url="user:login")
def index(request):
    tasks = models.Task.objects.filter(confirm="False",author=request.user).order_by('-id')
    form = TaskForm()

    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid:
            instance=form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect("/")
    context = {
        "tasks":tasks,
        "form":form,
    }
    return render(request,"index.html",context)


@login_required(login_url="user:login")
def updateTask(request,id):
    task = models.Task.objects.get(id=id)
    form = TaskForm(instance=task)

    if request.user == task.author:
        if request.method == "POST":
            form = TaskForm(request.POST,instance=task)
            if form.is_valid:
                form.save()
                return redirect("/")
    else:
        raise ValueError("Bu Task Sizin Deyil!")
    context = {
        "form":form,
    }
    return render(request,"update_task.html",context)

@login_required(login_url="user:login")
def deleteTask(request,id):
    task = models.Task.objects.get(id=id)
    
    if request.user == task.author:
        task.delete()
        return redirect("/")
    else:
        raise ValueError("Bu Task Sizin Deyil!")

    context = {
        "task":task,
    }
    return render(request,"delete_task.html",context)

@login_required(login_url="user:login")
def complededTasks(request):
    tasks = models.Task.objects.filter(confirm="True",author=request.user)

    context = {
        "tasks":tasks,
    }

    return render(request,"completeds.html",context)

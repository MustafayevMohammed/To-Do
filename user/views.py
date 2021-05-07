from django.core.exceptions import ValidationError
import user
from django.contrib.auth import authenticate, login
from django.shortcuts import render,redirect
from .forms import *
# Create your views here.

def registerPage(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("tasks:index")

    context = {"form":form}
    return render(request,"register.html",context)



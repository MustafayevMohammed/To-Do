from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate, login, logout
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


def loginPage(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request.POST)
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        account = authenticate(username=username,password=password)
        if account is None:
            raise ValidationError(request,"Parol Ya Da Istifadeci Adi Uygun Deyil!")
        else:
            login(request,account)
            return redirect("tasks:index")

    context = {
        "form":form,
    }
    return render(request,"login.html",context)


def logoutPage(request):
    logout(request)
    return redirect("tasks:index")
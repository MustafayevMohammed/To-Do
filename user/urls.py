from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from . views import *

app_name = "user"

urlpatterns = [
    path("register/",registerPage,name="register"),
    path("login/",loginPage,name="login"),
    path("logout/",logoutPage,name="logout"),
]
from django import forms
from django.db.models import fields
from django.forms import ModelForm, widgets
from django.forms.fields import CharField
from . import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ["username","password1","password2"]        
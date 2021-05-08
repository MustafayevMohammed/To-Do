from django.forms.forms import Form
from tasks.views import deleteTask
from django import forms
from django.db.models import fields
from django.forms import ModelForm, widgets
from django.forms.fields import CharField
from . import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):

    password1 = CharField(
        widget=forms.PasswordInput(attrs={'class':'passfields'})
    )
    password2 = CharField(
        widget=forms.PasswordInput(attrs={'class':'passfields'})
    )

    class Meta(UserCreationForm.Meta):
        model = User
        widgets = {
            'username': forms.TextInput(attrs={'class':'fields'}),
            'email': forms.TextInput(attrs={'class':'fields'}),
            

        }
        fields = ["password1","password2","username","email"]


class LoginForm(forms.Form):
    username = forms.CharField(required=True,widget=forms.TextInput(attrs={
        'class':"login-fields"
    }))
    password = forms.CharField(required=True,widget=forms.PasswordInput(attrs={
        "class":"login-fields"
    }))
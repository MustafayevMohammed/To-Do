from django import forms
from django.db.models import fields
from django.forms import ModelForm, widgets
from . import models

# Forms
class TaskForm(forms.ModelForm):
    class Meta:
        model = models.Task
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Task Daxil Edin:','class':'addbar','spellcheck':'false'}),
        }
        fields = "__all__"
        
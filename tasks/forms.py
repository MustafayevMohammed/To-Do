from django import forms
from django.db.models import fields
from django.forms import ModelForm, widgets
from . import models

# Forms
class TaskForm(forms.ModelForm):
    class Meta:
        model = models.Task
        widgets = {
            'title': forms.Textarea(attrs={'class':'addbar','spellcheck':'false','cols':81,'rows':4,'style':'resize:none;'}),
        }
        fields = "__all__"
        
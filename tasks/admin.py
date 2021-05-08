from django.contrib import admin
from . import models
# Register your models here.
@admin.register(models.Task)
class TaskAdmin(admin.ModelAdmin):
    
    list_display = ["id","title","author"]
    list_display_links = ["id","title"]
    class Meta:
        model = models.Task
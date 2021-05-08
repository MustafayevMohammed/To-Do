from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User
# Create your models here.
class Task(models.Model):
    author = models.ForeignKey(User ,on_delete=models.CASCADE ,null=True ,verbose_name="Yazan:",blank=True ,default=None)
    title = models.CharField(max_length=200,blank=False,verbose_name="Basliq:")
    created_date = models.DateTimeField(auto_now_add=True,verbose_name="Yazilma Tarixi:")
    confirm = models.BooleanField(default=False,verbose_name="Tamamlanilib?:")
    def __str__(self):
        return self.title

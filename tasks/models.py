from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=200,blank=False,verbose_name="Basliq:")
    created_date = models.DateTimeField(auto_now_add=True,verbose_name="Yazilma Tarixi:")
    confirm = models.BooleanField(default=False,verbose_name="Tamamlanilib?:")
    def __str__(self):
        return self.title

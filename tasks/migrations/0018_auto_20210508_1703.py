# Generated by Django 3.1.7 on 2021-05-08 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0017_auto_20210508_1648'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Basliq:'),
        ),
    ]
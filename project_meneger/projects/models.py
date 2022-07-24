from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Project(models.Model):
    name=models.CharField(max_length=50)
    describtion=models.TextField(default='')
    workers=models.ManyToManyField(User,blank=True)
    deadline=models.DateField(null=True,blank=True)
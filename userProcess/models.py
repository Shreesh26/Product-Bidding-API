from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

class Branch(models.Model):
    branch=models.CharField(max_length=30)
    def __str__(self):
        return self.branch

class UserDetail(models.Model):
    user=models.OneToOneField(User, on_delete= CASCADE)
    img=models.ImageField(upload_to="userProfile", blank=True)
    roll_number=models.CharField(max_length=15)
    name=models.CharField(max_length=20)
    #branch=models.ManyToManyField(Branch, on_delete=CASCADE)
    def __str__(self):
        return self.name+"-"+self.roll_number


from django.db import models
from django.contrib.auth.models import User


class Project(models.Model):
    title = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Entry(models.Model):
    duration = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    saved = models.BooleanField(default=False , null=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True )

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=255 , unique=True, null=False)
    email = models.EmailField(max_length=255, unique=True, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    name= models.CharField(max_length=255, null=True)





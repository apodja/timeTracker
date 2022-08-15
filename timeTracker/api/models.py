from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Entry(models.Model):
    duration = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null = True)
    saved = models.BooleanField(default=False , null=True)



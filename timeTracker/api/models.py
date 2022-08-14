from django.db import models



class Entry(models.Model):
    duration = models.IntegerField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
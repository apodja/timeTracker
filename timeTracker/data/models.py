from django.db import models
from django.contrib.auth.models import User

STATUS =(
    ('TODO', 'To-Do'),
    ('ONGOING', 'Ongoing'),
    ('DONE', 'Done')
)


class Project(models.Model):
    title = models.CharField(max_length=255)
    user = models.ForeignKey(User,related_name="projects", on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title

class Task(models.Model):
    title = title = models.CharField(max_length=255)
    assigned_users = models.ManyToManyField(User, related_name="tasks")
    project = models.ForeignKey(Project,related_name='tasks', on_delete=models.CASCADE)
    status = models.CharField(choices=STATUS,default="TODO",  max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title


class Entry(models.Model):
    duration = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    saved = models.BooleanField(default=False , null=True)
    task = models.ForeignKey(Task,related_name= 'entries', on_delete=models.CASCADE, null=True)

    def __str__(self) -> str:
        return f'{self.user.username} - {self.duration}'

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=255 , unique=True, null=False)
    email = models.EmailField(max_length=255, unique=True, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    name= models.CharField(max_length=255, null=True)

    def __str__(self) -> str:
        return self.username





from django.shortcuts import render
from data.models import *
from django.db.models import Sum

def index(request):
    projects = Project.objects.all().annotate(nr = Sum('tasks'))
    print()
    return render(request, 'projects/index.html')
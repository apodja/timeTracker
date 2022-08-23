import datetime
from django.shortcuts import render
from data.models import *
from django.db import connection

def index(request):
    cursor = connection.cursor()
    cursor.execute(''' SELECT data_project.id , data_project.title , COUNT(data_task.id) AS tasks , SUM(data_entry.duration) as total_time from data_project left JOIN data_task on data_project.id = data_task.project_id 
        JOIN data_entry on data_entry.task_id = data_task.id GROUP BY data_project.id  ORDER BY total_time DESC''')
    rows= cursor.fetchall()
    objects = []
    for row in rows:
        row_list = list(row)
        row_list[3] = str(datetime.timedelta(seconds=row_list[3]))
        objects.append(row_list)
    return render(request, 'projects/index.html', context = {'projects' : objects} )

def project(request,pk):
    todos = Task.objects.filter(project_id = pk , status = "TODO").order_by('-created_at')
    ongoing = Task.objects.filter(project_id = pk , status = "ONGOING").order_by('-created_at')
    done = Task.objects.filter(project_id = pk , status = "DONE").order_by('-created_at')
    context = {
        'todos' : todos ,
        'ongoing' : ongoing , 
        'done' : done
    }
    return render(request , 'projects/project.html', context)

from django.shortcuts import render
from data.models import *
from django.db.models import Sum,Count
from django.db import connection

def index(request):
    # projects = Project.objects.all().annotate(nr = Count('tasks'))
    # projects = Project.objects.raw("SELECT data_project.id, data_project.title , count(data_task.id) , SUM(data_entry.duration) as count FROM data_project inner join data_task on data_project.id = data_task.project_id right join data_entry on data_entry.task_id = data_task.id group by data_project.id , data_task.id ")
    # for p in projects:
    #     print(p.title)

    # cursor = connection.cursor()
    # cursor.execute(''' SELECT data_project.id, data_project.title , count(data_task.id) as count_tasks , SUM(data_entry.duration) as count_time FROM data_project inner join data_task on data_project.id = data_task.project_id left join data_entry on data_entry.task_id = data_task.id group by data_project.id ''')
    # rows= cursor.fetchall()
    # for row in rows:
    #     print(row)

    proj = Project.objects.all().extra(select={'count': 'count(project_id)'}).select_related()
    for p in proj :
        
        print(p['count'])

    return render(request, 'projects/index.html' )
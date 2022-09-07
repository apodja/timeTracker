import datetime
from django.shortcuts import render,redirect
from data.models import *
from django.db import connection
from django.http import HttpResponse, JsonResponse

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
    project = Project.objects.get(id=pk)
    todos = Task.objects.filter(project_id = pk , status = "TODO").order_by('-created_at')
    ongoing = Task.objects.filter(project_id = pk , status = "ONGOING").order_by('-created_at')
    done = Task.objects.filter(project_id = pk , status = "DONE").order_by('-created_at')
    context = {
        'todos' : todos ,
        'ongoing' : ongoing , 
        'done' : done,
        'project' : project
    }
    return render(request , 'projects/project.html', context)


def add_task(request):
    if request.method == 'POST' : 
        project_id = request.POST.get('project_id')
        task_desc = request.POST.get('title')
        if task_desc != "" and project_id is not None:
            project = Project.objects.get(id = project_id)
            task = Task.objects.create(project = project , title = task_desc)
            task.save()
            return redirect('project', pk = project_id)
        else:
            return HttpResponse('Error ...')    
    else:
        return HttpResponse('Error ...')


def delete_task(request,project_id,task_id):
    try : 
        # project = Project.objects.get(id = project_id)
        task = Task.objects.get(id = task_id)
        task.delete()
        return redirect('project', pk = project_id)
    except:
        return HttpResponse('Error')

    






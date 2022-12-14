from django.shortcuts import render
from data.models import Entry,Task
from django.utils import timezone
from django.db.models import Sum
from django.contrib.auth.decorators import login_required
import datetime

@login_required
def dashboard(request):

    user = request.user

    filter = request.GET.get('filter')
    if filter is not None :
        if filter == 'day':
            tasks  = Task.objects.filter(assigned_users = user, created_at__date= timezone.now()).count()
            total = Entry.objects.filter(user=user , created_at__date= timezone.now()).aggregate(Sum('duration'))
            if total['duration__sum'] is not None:
                time = str(datetime.timedelta(seconds = total['duration__sum']))
            else:
                time= 0
            context ={'tasks' : tasks ,  'total': time}
        elif filter == 'month':
            tasks  = Task.objects.filter(assigned_users = user, created_at__month = timezone.now().month).count()
            total = Entry.objects.filter(user=user , created_at__month= timezone.now().month).aggregate(Sum('duration'))
            if total['duration__sum'] is not None:
                time = str(datetime.timedelta(seconds = total['duration__sum']))
            else:
                time= 0
            context ={'tasks' : tasks ,  'total': time}
    else:
        tasks  = Task.objects.filter(assigned_users = user).count()

        total = Entry.objects.filter(user=user).aggregate(Sum('duration'))
        if total['duration__sum'] is not None:
            time = str(datetime.timedelta(seconds = total['duration__sum']))
        else:
            time= 0
        context ={ 'total': time, 'tasks': tasks}

    return render(request, 'dashboard/pages/index.html', context)


@login_required
def timer(request):
    return render(request,'dashboard/pages/timer.html')
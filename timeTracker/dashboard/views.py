
from django.shortcuts import render
from data.models import Entry
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
            entries = Entry.objects.filter(user=user , created_at__date= timezone.now())
            total = Entry.objects.filter(user=user , created_at__date= timezone.now()).aggregate(Sum('duration'))
            if total['duration__sum'] is not None:
                time = str(datetime.timedelta(seconds = total['duration__sum']))
            else:
                time= 0
            context ={'data' : entries ,  'total': time}
        elif filter == 'month':
            entries = Entry.objects.filter(user = user , created_at__month = timezone.now().month)
            total = Entry.objects.filter(user=user , created_at__month= timezone.now().month).aggregate(Sum('duration'))
            if total['duration__sum'] is not None:
                time = str(datetime.timedelta(seconds = total['duration__sum']))
            else:
                time= 0
            context ={'data' : entries ,  'total': time}
    else:
        entries = Entry.objects.filter(user=user)
        total = Entry.objects.filter(user=user).aggregate(Sum('duration'))
        if total['duration__sum'] is not None:
            time = str(datetime.timedelta(seconds = total['duration__sum']))
        else:
            time= 0
        context ={'data' : entries ,  'total': time}

    return render(request, 'dashboard/pages/index.html', context)


def timer(request):
    return render(request,'dashboard/pages/timer.html')
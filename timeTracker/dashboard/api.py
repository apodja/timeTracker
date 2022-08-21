from django.http import JsonResponse
from data.models import Entry
from django.utils import timezone
from rest_framework.views import APIView, Response
from rest_framework import permissions
from django.db.models import Sum
from data.serializers import EntrySerializer




def action(request):
    user = request.user
    try:
        entry = Entry.objects.get(user = user , duration = 0 , saved = False)
        delta = timezone.now() - entry.created_at
        sec = delta.seconds
        entry.duration = sec
        entry.saved = True
        entry.save()
        return JsonResponse({'success': True, 'info':'clock stopped'})
    except:
        entry = Entry.objects.create(user = user)
        return JsonResponse({'success': True, 'info':'clock started'})


class EntriesView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self,request, format=None):
        user = self.request.user
        
        filter = self.request.query_params.get('filter')
        if filter is not None :
            if filter == 'day':
                entries = Entry.objects.filter(user=user , created_at__date= timezone.now())
                serializer = EntrySerializer(entries, many = True)
                total = Entry.objects.filter(user=user , created_at__date= timezone.now()).aggregate(Sum('duration'))
                return Response({'data' : serializer.data ,  'total':total['duration__sum']})
            elif filter == 'month':
                entries = Entry.objects.filter(user = user , created_at__month = timezone.now().month)
                serializer = EntrySerializer(entries, many = True)
                total = Entry.objects.filter(user=user , created_at__month= timezone.now().month).aggregate(Sum('duration'))
                return Response({'data' : serializer.data ,  'total':total['duration__sum']})
        entries = Entry.objects.filter(user=user)
        serializer = EntrySerializer(entries, many = True)
        return Response({'data' : serializer.data ,  'total':total['duration__sum']})



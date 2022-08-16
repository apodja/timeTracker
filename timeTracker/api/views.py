from django.http import JsonResponse
from .models import Entry
from django.utils import timezone
from .serializers import EntrySerializer
from rest_framework.views import APIView, Response
from rest_framework import permissions
from datetime import datetime



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
        user = request.user
        entries = Entry.objects.filter(user = user)
        serializer = EntrySerializer(entries, many = True)
        return Response(serializer.data)



    # def get(self,request, format=None):
    #     user = request.user
    #     today = datetime.today()
    #     year = today.year
    #     month = today.month
    #     day = today.day
    #     print(year)
    #     print(month)
    #     filter = self.request.query_params.get('filter')
    #     print(filter)
    #     if filter is not None :
    #         print('filter')
    #         if filter == 'month':
    #             entries = Entry.objects.filter(user = user, created_at__year=year, created_at__month=month, created_at__day=day )
    #             print('ok')
    #         entries = Entry.objects.filter(user = user, created_at__year = year )
    #     entries = Entry.objects.filter(user = user, created_at__day = day )
    #     print('no filter')
    #     serializer = EntrySerializer(entries, many = True)
    #     return Response(serializer.data)



    










# def startTime(request):
#     user = request.user
#     try:
#         entry = Entry.objects.get(user = user , duration = 0 , saved = False)
#         return JsonResponse({'warning': 'you have a session open'})
#     except:
#         entry = Entry.objects.create(user = user)
#         return JsonResponse({'success': True})
    

# def stopTime(request):
#     user = request.user
#     try: 
#         entry = Entry.objects.get(user = user , duration = 0 , saved = False)
#         delta = timezone.now() - entry.created_at
#         sec = delta.seconds
#         entry.duration = sec
#         entry.saved = True
#         entry.save()
#         return JsonResponse({'ora': sec , 'success': 'Time stopped and saved'})
#     except:
#         return JsonResponse({'error': 'You have no session open '})
        

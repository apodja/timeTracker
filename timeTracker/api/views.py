from django.http import JsonResponse
from .models import Entry
from django.utils import timezone


# class startStop(APIView):
#     authentication_classes = []
#     def post(self , request , *args, **kwargs):
#         a= request.data.get('ora')
#         if a != None or a > 0 :
#             entry = Entry.objects.create(duration = int(a))
#             entry.save()
#             return Response({'Success' : 'Time Tracked'})
#         return Response({'Error' : 'Bad response'})


def startTime(request):
    user = request.user
    try:
        entry = Entry.objects.get(user = user , duration = 0 , saved = False)
        return JsonResponse({'warning': 'you have a session open'})
    except:
        entry = Entry.objects.create(user = user)
        return JsonResponse({'success': True})
    

def stopTime(request):
    user = request.user
    try: 
        entry = Entry.objects.get(user = user , duration = 0 , saved = False)
        delta = timezone.now() - entry.created_at
        sec = delta.seconds
        entry.duration = sec
        entry.saved = True
        entry.save()
        return JsonResponse({'ora': sec , 'success': 'Time stopped and saved'})
    except:
        return JsonResponse({'error': 'You have no session open '})
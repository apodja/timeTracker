from django.shortcuts import render
from rest_framework.views import APIView, Response 
from .models import Entry


class index(APIView):
    authentication_classes = []
    def post(self , request , *args, **kwargs):
        a= request.data.get('ora')
        if a != None or a > 0 :
            entry = Entry.objects.create(duration = int(a))
            entry.save()
            return Response({'Success' : 'Time Tracked'})
        return Response({'Error' : 'Bad response'})

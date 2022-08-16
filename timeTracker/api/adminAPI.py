from django.http import JsonResponse
from .models import Entry
from django.utils import timezone
from .serializers import EntrySerializer
from rest_framework.views import APIView, Response
from rest_framework import permissions
from datetime import datetime



class EntriesViewAdmin(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self,request, format=None):
        entries = Entry.objects.all()
        serializer = EntrySerializer(entries, many = True)
        print(request.query_params)
        return Response(serializer.data)

        

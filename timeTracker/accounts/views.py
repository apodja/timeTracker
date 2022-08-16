
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions
from django.contrib.auth import authenticate, login

class CheckAuthenticatedView(APIView):
    def get(self, request, format=None):
        user = self.request.user

        try:
            isAuthenticated = user.is_authenticated

            if isAuthenticated:
                return Response({ 'isAuthenticated': 'success' })
            else:
                return Response({ 'isAuthenticated': 'error' })
        except:
            return Response({ 'error': 'Something went wrong when checking authentication status' })

class LoginView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self,request, format = None):
        data = request.data
        username = data['username']
        password = data['password']

        try : 
            user = authenticate( username = username,password = password)
            if user : 
                login(self.request,user)
                return Response({'success' : 'logged in'})
            return Response({'error' : 'invalid credentials'})
        except:
            return Response({'error' : 'an error occurred'})
            


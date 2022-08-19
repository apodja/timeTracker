from django.shortcuts import render,redirect
from rest_framework.response import Response
from rest_framework.views import APIView, status
from rest_framework import permissions
from django.contrib.auth import authenticate, login
from django .contrib import messages

class CheckAuthenticatedView(APIView):
    def get(self, request, format=None):
        user = self.request.user

        try:
            isAuthenticated = user.is_authenticated

            if isAuthenticated:
                    return Response({ 'isAuthenticated': 'success'}, status = status.HTTP_200_OK )
            else:
                return Response({ 'isAuthenticated': 'error' })
        except:
            return Response({ 'error': 'Something went wrong when checking authentication status' })

# class LoginView(APIView):
#     permission_classes = [permissions.AllowAny]

#     def post(self,request, format = None):
#         data = request.data
#         username = data['username']
#         password = data['password']

#         try : 
#             user = authenticate( username = username,password = password)
#             if user : 
#                 login(self.request,user)
#                 return Response({'success' : True}, status = status.HTTP_200_OK)
#             return Response({'success' : False })
#         except:
#             return Response({'succes' : False})



def loginUser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(password)

        user = authenticate( username = username ,password = password)
        if user :
            login(request, user)
            print('logged in')
            return redirect('/dashboard')
        else : 
            print('no')

    return render(request, 'accounts/login.html')
            


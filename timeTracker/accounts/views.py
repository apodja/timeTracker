from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User
from data.models import UserProfile



def loginUser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate( username = username ,password = password)
        if user :
            login(request, user)
            return redirect('dashboard')
        else : 
            messages.error(request, 'Invalid credentials!')

    return render(request, 'accounts/login.html')
            

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        if User.objects.filter(username=username).exists():
            messages.warning(request, 'User with this username already exists')
        elif User.objects.filter(email=email).exists():
            messages.warning(request, 'User with this email already exists')
        else :
           user = User.objects.create_user(username = username, email = email, password=password)
           profile = UserProfile.objects.create(user = user,username = username, email = email)
           messages.success(request, 'User created successfully ! Login now!') 
           return redirect('login')
    else:
        messages.error(request, 'An error occurred !')
    return render(request, 'accounts/register.html')
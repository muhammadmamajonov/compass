from django.shortcuts import render, redirect
# from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User, auth
from django.contrib import messages
# Create your views here.

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            if user.is_superuser:
                return redirect('/dashboard')
            else:
                return redirect('/dashboard/oqituvchi-dash')
        else:
            messages.info(request, "Login yoki Parol Xato")
            
        return render(request, 'login.html')
    return render(request, 'login.html')

def chiqish(request):
    auth.logout(request)
    return redirect('/login')
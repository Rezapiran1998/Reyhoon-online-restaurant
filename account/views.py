from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib import auth
from django.contrib.auth.models import User

def login(request):
    if request.method == 'POST':
        user = authenticate(
            username=request.POST['logEmail'], password=request.POST['logEmail'])
        if user is not None:
            auth.login(request, user)
            return redirect('login')
        else:
            return render(request, 'login.html', {'error': 'Password or username  not match'})
    return render(request, 'login.html')

def logout(request): 
    logout(request)
    
    # Redirect to a success page.

def register(request):
    if request.method == 'POST':
        if request.POST["signPass1"] == request.POST["signPass2"]:
            try:
                User.objects.get(username=request.POST["signUsername"])
                return render(request, 'signin.html', {'error': 'Username  has already been taken'})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST["signEmail"],
                    request.POST["signUsername"], password=request.POST["signPass1"])
                return redirect('login')

        else:
            return render(request, 'signin.html', {'error': 'Passwords do not match'})
    else:
         return render(request, 'signin.html')
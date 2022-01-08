from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.hashers import check_password

def login_view(request):
    if request.method == 'POST':
        email=request.POST['logEmail']
        password=request.POST['logPassword']
        user = User.objects.filter(email=email).first()
        # print(user)


        if user is not None and check_password(password, user.password) and user.is_active:
            auth.login(request, user)
            messages.success(request, 'کابر با موفقیت وارد شد')
            return redirect('index')

        else:
            return render(request, 'login.html', {'error': 'ایمیل یا پسورد اشتباه است'})
    return render(request, 'login.html',{'success':'کاربر وارد شد'})

def logout(request): 
    logout(request)
    
def register(request):
    if request.method == 'POST':
        if request.POST["signPass1"] == request.POST["signPass2"]:
            try:
                User.objects.get(email=request.POST["signEmail"])
                return render(request, 'signin.html', {'error': 'کاربری با این مشخصات موجود هست'})
            except User.DoesNotExist:
                user = User.objects.create_user(email = request.POST["signEmail"],
                    username = request.POST["signUsername"], password=request.POST["signPass1"])
                messages.success(request, 'کابر با موفقیت ایجاد شد')
                return redirect('login')
            except:
                return render(request, 'signin.html', {'error': 'کاربری با این مشخصات موجود هست'})


        else:
            return render(request, 'signin.html', {'error': 'پسورد های وارد شده باید یکسان باشند'})
    else:
         return render(request, 'signin.html',{'success':'کاربر جدید با موفقیت ایجاد شد'})
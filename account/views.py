from django.shortcuts import render

def login(request):
    return render(request, 'signin.html', {})

def register(request):
    return render(request, 'signin.html', {})

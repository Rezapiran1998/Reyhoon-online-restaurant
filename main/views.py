from django.shortcuts import render
from django.http import Http404

def index(request):

    return render(request, 'index.html', {})


def restaurant(request):
    return render(request, 'resturantListPage.html', {})
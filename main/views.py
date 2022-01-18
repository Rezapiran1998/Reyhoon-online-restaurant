from django.shortcuts import render
from django.http import Http404
from .models import Resturant
from django.core.paginator import Paginator

def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

def index(request):

    return render(request, 'index.html', {})


def restaurant(request):

    if('q' in request.GET):
        resturants = Resturant.objects.filter(name__icontains=request.GET['q'])
    else:
        resturants = Resturant.objects.all()

    resturants = Paginator(resturants, 9)

    # resturants = list(chunks(resturants, 3))

    page_number = request.GET.get('page', 1)
    resturants = resturants.get_page(page_number)

    return render(request, 'resturantListPage.html', {
        'resturants': resturants,
        'rate_range': [80, 60, 40, 20, 0],
    })
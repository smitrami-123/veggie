from django.shortcuts import render
from .models import Carousel
# Create your views here.
def index(request):
    items = Carousel.objects.all()
    context = {
        'items' : items
    }
    return render(request, 'home/index.html', context)

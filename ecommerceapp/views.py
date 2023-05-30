from django.shortcuts import render
from .models import Product

# Create your views here.


def index(request):
    items = Product.objects.values('pk','name','price','image')
    context = {
        'items': items
    }
    return render(request, "home.html", context)


from django.shortcuts import render
from .models import Item

# Create your views here.

def home(request):
    all_items = Item.objects.all
    return render(request, 'home.html', {'all' : all_items})

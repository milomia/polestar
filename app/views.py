from django.shortcuts import render
from django.http import HttpResponse
import pdb as pdb_module
from django.template import Library, Node

from app.models import Position

def home(request):
    ships = Position.objects.all()
    return render(request,'home.html',{'ships': ships })

def ships(request):
    ships = Position.objects.all()
    return render(request,'home.html',{'ships': ships })

def index(request):
    ships = Position.objects.all()
    return render(request,'home.html',{'ships': ships })

def positions(request):
    ships = Position.objects.all()
    return render(request,'home.html',{'ships': ships })

def ship_detail(request, id):
    try:
        ship = Position.objects.get(id=1)
    except Position.DoesNotExist:
        raise Http404('Position not found')
    return render(request, 'ship_detail.html', {'ship':ship})

def ship_position(request, id):
    try:
        ship = Position.objects.get(id=1)
    except Position.DoesNotExist:
        raise Http404('Position not found')
    return render(request, 'ship_detail.html', {'ship':ship})

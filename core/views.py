from django.shortcuts import render
from .models import Event

# Create your views here.
def eventos(request):
    evento = Event.objects.all()
    data = {
        'eventos':evento
    }
    return render(request, 'core/eventos.html', data)


def world_party(request):
    
    return render(request, 'core/worldparty.html')

def objetivos(request):
    
    return render(request, 'core/objetivos.html')

def flaghunters(request):
    
    return render(request, 'core/flaghunters.html')


def hackerspace(request):
    
    return render(request, 'core/hackerspace.html')

def colaboracion(request):
    
    return render(request, 'core/colaboracion.html')

def conferencias(request):
    
    return render(request, 'core/conferencias.html')


def cfpblack(request):
    
    return render(request, 'core/cfp-black.html')

def home(request):
    evento = Event.objects.all()
    data = {
        'eventos':evento
    }
    return render(request, 'core/home.html', data)


def login(request):
    
    return render(request, 'core/admin/login.html')
   
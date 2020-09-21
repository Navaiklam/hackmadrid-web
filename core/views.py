from django.shortcuts import render
from .models import Event

# Create your views here.
def eventos(request):
    evento = Event.objects.all()
    data = {
        'eventos':evento
    }
    return render(request, 'core/eventos.html', data)

def cfpblack(request):

    return render(request, 'core/cfp-black.html')

def home(request):
    evento = Event.objects.all()
    data = {
        'eventos':evento
    }
    return render(request, 'core/home.html', data)
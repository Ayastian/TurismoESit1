from django.shortcuts import render
from .models import Servicios

# Create your views here.
def index(request):
    context = {}
    return render(request, 'turismo/index.html', context)

def servicios(request):
        servicios = Servicios.objects.all()
        context = {'servicios': servicios}
        return render(request, 'turismo/servicios.html', context)
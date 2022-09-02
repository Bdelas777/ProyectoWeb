from django.shortcuts import render
from servicios.models import Servicio
# Create your views here.

def servicios(request):
    # Cargar la libreria peeling para evitar errores
    servicios = Servicio.objects.all()
    
    return render(request, "servicios/servicios.html",{"servicios":servicios})
from django.shortcuts import render, HttpResponse

# Create your views here.
# Boostrap formatos css  y es responsive compatible para todos los navegadores
''' Crear una web bien organizada
reutilizacion de elementos web
diseño adaptable
crea grids
comunidad activa
uso en cms
uso de less'''
def home(request):
    
    return render(request, "ProyectoWebapp/home.html")

def tienda(request):
    
    return render(request, "ProyectoWebapp/tienda.html")


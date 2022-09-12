from django.shortcuts import render

# Create your views here.
# Uso de la libreria forms
def contacto(request):
    
    return render(request, "contacto/contacto.html")
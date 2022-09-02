"""ProyectoWeb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('servicios/', include('servicios.urls')),
    path('blog/', include('blog.urls')),
    path('',include('ProyectoWebapp.urls')),
]
'''
Mapeo o rm que es mapeo de objetos el cual consiste en que tu crees el 
modelo y de ahi creas una clase con atributos que quieres que aparezcan 
en la tabla cada atributo correspondera a un campo de la tabla donde se
guarda la info.en nuestro caso de un servicio de mapeo rm consiste en crear
un objeto desde codigo y ese objeto representara a un objeto en una tabla 
con sus propiedades es utilizar poo pa poder manipular el cod de python en este caso el de las tablas con campos y registros
'''
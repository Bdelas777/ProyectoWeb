from ssl import create_default_context
from tabnanny import verbose
from django.db import models

# Create your models here.

class Servicio(models.Model):
    titulo = models.CharField( max_length = 50)
    contenido = models.CharField( max_length = 50)
    imagen = models.ImageField(upload_to = 'servicios')
    # Campos de orden
    created  = models.DateTimeField( auto_now_add =  True )
    updated  = models.DateTimeField( auto_now_add =  True )
    
    # Meta opciones de modelo
    class Meta:
        verbose_name = 'servicio' # Nombre de la tabla
        verbose_name_plural = 'servicios' # Nombre de los campos
        
    def __str__(self) :
        return self.titulo
        
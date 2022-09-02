from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Categoria (models.Model):
    nombre = models.CharField( max_length = 50)
    created  = models.DateTimeField( auto_now_add =  True )
    updated  = models.DateTimeField( auto_now_add =  True )
    
    # Meta opciones de modelo
    class Meta:
        verbose_name = 'categoria' # Nombre de la tabla
        verbose_name_plural = 'categorias' # Nombre de los campos
        
    def __str__(self) :
        return self.nombre
        
class Post (models.Model):
    titulo = models.CharField( max_length = 50)
    contenido = models.CharField( max_length = 50)
    imagen = models.ImageField(upload_to = 'blog', null= True, blank= True)
    autor = models.ForeignKey(User, on_delete = models.CASCADE)
    categorias = models.ManyToManyField(Categoria)
    created  = models.DateTimeField( auto_now_add =  True )
    updated  = models.DateTimeField( auto_now_add =  True )
    
    # Meta opciones de modelo
    class Meta:
        verbose_name = 'post' # Nombre de la tabla
        verbose_name_plural = 'posts' # Nombre de los campos
        
    def __str__(self) :
        return self.titulo
from django.contrib import admin
from .models import Productos, CategoriaProd
# Register your models here.

class CategoriaProdAdmin(admin.ModelAdmin):
    readonly_fields = ("created","updated")
    
class ProductosAdmin(admin.ModelAdmin):
    readonly_fields = ("created","updated")

admin.site.register(CategoriaProd,CategoriaProdAdmin)

admin.site.register(Productos, ProductosAdmin)
from django.contrib import admin
from .models import Oferta
from django.contrib.auth.models import Group, Permission

# Register your models here.
@admin.register(Oferta)

class OfertaAdmin(admin.ModelAdmin):
    list_display = ('producto', 'porcentaje_descuento', 'fecha_inicio', 'fecha_fin')
    search_fields = ('producto__nombre', )
    
    def save_model(self,request, obj, form, change):
        group_admin = Group.objects.get(name='Administradores')
        permisos = Permission.objects.filter(codename__in=['Crear_Ofertas', 'Editar_Ofertas', 'Eliminar_Ofertas'])
        
        group_admin.permissions.add(*permisos)
        
        
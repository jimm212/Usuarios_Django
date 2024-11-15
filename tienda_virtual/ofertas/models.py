from typing import Iterable
from django.db import models
from django.forms import ValidationError
from productos.models import Productos

# Create your models here.
class Oferta(models.Model):
    producto = models.ForeignKey(Productos, on_delete=models.CASCADE)
    porcentaje_descuento = models.DecimalField(max_digits=5, decimal_places=2)
    fecha_inicio = models.DateTimeField()
    fecha_fin = models.DateTimeField()
    
    def clean(self):
        if self.fecha_inicio>=self.fecha_fin:
            raise ValidationError("La fecha de inicio de la oferta debe ser anterior a la fecha de fin.")
        if self.porcentaje_descuento<0 or self.porcentaje_descuento>100:
            raise ValidationError("El porcentaje de descuento debe estar entre 0 y 100.")
        
    def save(self, *args, **kwargs):
        # LLama a la función clean para validar los datos antes de guardarlos
        self.clean()
        super(Oferta, self).save(*args, **kwargs)
    
    
    def __str__(self):
        return f" oferta en: {self.producto.nombre} --- Descuento: {self.porcentaje_descuento}% "
    
    @property
    def precio_descuento(self):
        return self.producto.precio * (1 - self.porcentaje_descuento/100)

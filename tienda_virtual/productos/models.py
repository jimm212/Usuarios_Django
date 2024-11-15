from django.db import models

# Create your models here.

class Categorias(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Productos(models.Model):
    nombre = models.CharField(max_length=200)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    Categoria = models.ForeignKey(Categorias, on_delete=models.CASCADE)
        
    def __str__(self):
        return self.nombre
    
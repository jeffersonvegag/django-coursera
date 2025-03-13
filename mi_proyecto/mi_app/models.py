from django.db import models

# Create your models here.

class Categoria(models.Model):
    nombre=models.CharField(max_length=100)
    descripcion= models.CharField()

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre
    
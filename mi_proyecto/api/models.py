from django.db import models
from django.core.validators import MaxValueValidator
class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    
    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.ForeignKey(Categoria, related_name='productos', on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    disponible = models.BooleanField(default=True)
    #se agregar max value validator
    stock = models.IntegerField(
        validators=[MaxValueValidator(3000)],
        null=True,
        blank=True,
        default=None
    )
    
    def __str__(self):
        return self.nombre
from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator    

# Create your models here.
class Tarea(models.Model):
    titulo = models.CharField(max_length=120)
    descripcion = models.TextField()
    prioridad = models.IntegerField(validators=[MinValueValidator(3)])
    vigente = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(default=timezone.now)
    fecha_limite = models.DateField(null=True, blank=True)


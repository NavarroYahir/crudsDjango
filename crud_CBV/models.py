from django.db import models

class Cosa(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True, null=True)
    involucrados = models.DecimalField(max_digits=10 ,decimal_places=2)

    def __str__(self):
        return self.nombre
from django.db import models

# Create your models here.

class Familiares(models.Model):
    Nombre = models.CharField(max_length=35)
    Apellido = models.CharField(max_length=35)
    DNI = models.IntegerField()
    Profesion = models.CharField(max_length=35)
    FechaDeNacimineto = models.DateField()

    def NombreCompleto(self):
        cadena='{0} {1}'
        return cadena.format(self.Nombre,self.Apellido)

    def __str__(self):
        return self.NombreCompleto()

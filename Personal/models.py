from django.db import models

class Colaboradores(models.Model):
    Nombre = models.CharField(max_length=20)
    Apellido = models.CharField(max_length=20)
    NumeroLegajo = models.IntegerField()
    NumeroDocumento = models.IntegerField(primary_key=True)
    Cargo = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.Nombre}, {self.Apellido}, {self.NumeroLegajo}, {self.NumeroDocumento}, {self.Cargo}"
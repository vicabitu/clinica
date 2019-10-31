from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    es_medico = models.BooleanField(default=False)
    es_paciente = models.BooleanField(default=False)

class Medico(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, blank=True, null=True)
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    especialidad = models.CharField(max_length=30)

class Paciente(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, blank=True, null=True)
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    direccion = models.CharField(max_length=30)
    telefono = models.CharField(max_length=30)
    fecha_de_nacimiento = models.DateField()
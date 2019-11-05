from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    es_medico = models.BooleanField(default=False)
    es_paciente = models.BooleanField(default=False)

    def __str__(self):
        if self.es_medico:
            cadena = "Medico"
        else:
            cadena = "Paciente"
        return "{} - {} - {}".format(self.first_name, self.last_name, cadena)

    def get_view_name(self):
        if self.es_medico:
            return 'medico'
        else:
            return 'paciente'


class Medico(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, blank=True, null=True)
    especialidad = models.CharField(max_length=30)

    def __str__(self):
        return  "{} - {} - {}".format(self.usuario.first_name, self.usuario.last_name, self.especialidad)

class Paciente(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, blank=True, null=True)
    direccion = models.CharField(max_length=30)
    telefono = models.CharField(max_length=30)
    fecha_de_nacimiento = models.DateField(blank=True, null=True)

    def __str__(self):
        return "{} - {}".format(self.usuario.first_name, self.usuario.last_name)
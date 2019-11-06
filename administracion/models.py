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

class Paciente(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, blank=True, null=True)
    direccion = models.CharField(max_length=30)
    telefono = models.CharField(max_length=30)
    fecha_de_nacimiento = models.DateField(blank=True, null=True)
    obra_social = models.CharField(max_length=35, blank=True, null=True)
    edad = models.PositiveSmallIntegerField(blank=True, null=True)
    dni = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        return "{} - {}".format(self.usuario.first_name, self.usuario.last_name)

class Medico(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, blank=True, null=True)
    # pacientes = models.ManyToManyField(Paciente, symmetrical=False)
    especialidad = models.CharField(max_length=30, blank=True, null=True)
    matricula = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return  "{} - {} - {}".format(self.usuario.first_name, self.usuario.last_name, self.especialidad)


class HistoriaMedica(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, null=True, related_name='historias_medicas')
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE, null=True, related_name='historias_medicas')

    def __str__(self):
        return "{} {} {} {}".format("Medico: ", self.medico.__str__(), " - Paciente: ", self.paciente.__str__())
    

class DetalleHistoriaMedica(models.Model):
    historia_medica = models.ForeignKey(HistoriaMedica, on_delete=models.CASCADE, null=True, related_name='detalles')
    fecha = models.DateField(blank=True, null=True)
    observaciones = models.TextField(blank=True, null=True)
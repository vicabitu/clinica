from django.contrib import admin
from .models import *

admin.site.register(Usuario)
admin.site.register(Medico)
admin.site.register(Paciente)
admin.site.register(HistoriaMedica)
admin.site.register(DetalleHistoriaMedica)
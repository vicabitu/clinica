from django.urls import path, include
from . import views

urlpatterns = [
    path('medico', views.mostrar_index_medico, name='medico'),
    path('paciente', views.mostrar_index_paciente, name='paciente'),
    path('historias_medicas_medico', views.ListarHistoriasClinicasMedico.as_view(), name='historias_medicas_medico'),
    path('pacientes', views.ListarPacientes.as_view(), name='pacientes'),
    path('detalle_historia_medica/<int:pk>', views.ListadoDetalleHistoriaMedicaPaciente.as_view(), name='detalle_historia_medica'),
    path('historias_medicas_paciente', views.ListarHistoriasClinicasPaciente.as_view(), name='historias_medicas_paciente'),
]
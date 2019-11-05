from django.urls import path, include
from . import views

urlpatterns = [
    path('medico', views.mostrar_index_medico, name='medico'),
    path('paciente', views.mostrar_index_paciente, name='paciente')
]
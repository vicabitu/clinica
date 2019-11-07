from django.shortcuts import render
from django.views.generic import View, CreateView, ListView, DetailView, TemplateView, FormView
from .models import HistoriaMedica, Paciente

def mostrar_index_medico(request):
    return render(request, 'medico/medico.html')

def mostrar_index_paciente(request):
    return render(request, 'paciente/paciente.html')

class ListarHistoriasClinicasMedico(ListView):
    model = HistoriaMedica
    template_name = 'medico/historias_medicas.html'
    context_object_name = 'historias_medicas'

    def get_queryset(self):
        return HistoriaMedica.objects.filter(medico=self.request.user.medico)

class ListarPacientes(ListView):
    model = Paciente
    template_name = 'medico/pacientes.html'
    context_object_name = 'pacientes'

    def get_queryset(self):
        return Paciente.objects.filter(historias_medicas__medico=self.request.user.medico)

class DetalleHistoriaMedica(DetailView):
    model = HistoriaMedica
    template_name = 'medico/detalle_historia_medica.html'
    context_object_name = 'historia'
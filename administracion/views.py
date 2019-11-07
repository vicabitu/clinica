from django.shortcuts import render
from django.views.generic import View, CreateView, ListView, DetailView, TemplateView, FormView
from .models import HistoriaMedica, Paciente, DetalleHistoriaMedica

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

class ListadoDetalleHistoriaMedicaPaciente(ListView):
    model = DetalleHistoriaMedica
    template_name = 'paciente/detalle_historia_medica.html'
    context_object_name = 'detalles'

    def get_queryset(self, **kwargs):
        pk = self.kwargs['pk']
        historia_medica = HistoriaMedica.objects.get(pk=pk)
        print(DetalleHistoriaMedica.objects.filter(historia_medica=historia_medica))
        return historia_medica.detalles.all()

class ListarHistoriasClinicasPaciente(ListView):
    model = HistoriaMedica
    template_name = 'paciente/historias_medicas.html'
    context_object_name = 'historias_medicas'

    def get_queryset(self):
        return HistoriaMedica.objects.filter(paciente=self.request.user.paciente)
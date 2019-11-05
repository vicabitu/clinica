from django.shortcuts import render

def mostrar_index_medico(request):
    return render(request, 'medico/medico.html')

def mostrar_index_paciente(request):
    return render(request, 'paciente/paciente.html')

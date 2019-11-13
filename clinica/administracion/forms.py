from django import forms
from .models import Paciente, Medico
from django.contrib.auth.forms import UserCreationForm

class FormularioEditarPaciente(forms.ModelForm):
    
    class Meta:
        model = Paciente

        fields = [
            'dni',
            'direccion',
            'telefono',
            'fecha_de_nacimiento',
            'obra_social',
            'edad'
        ]
        widgets = {
            'dni': forms.TextInput(attrs={'class':'form-control', 'placeholder':'DNI'}),
            'direccion': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Direccion'}),
            'telefono': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Telefono'}),
            'fecha_de_nacimiento': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Fecha de Nacimiento'}),
            'obra_social': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Obra social'}),
            'edad': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Edad'})
        }

class FormularioEditarMedico(forms.ModelForm):
    class Meta:
        model = Medico

        fields = [
            'especialidad',
            'matricula'
        ]

        widgets = {
            'especialidad': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Especialidad'}),
            'matricula': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Matricula'})
        }

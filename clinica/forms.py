from django import forms
from django.contrib.auth.forms import UserCreationForm
from administracion.models import Usuario
from django.db import transaction
from django.forms import ModelForm

class FormularioMedico(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder':'Contraseña'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder':'Repetir contraseña'}))

    class Meta:
        model = Usuario
        fields = [
            'first_name',
            'last_name',
            'username',
            'password1', 
            'password2'
        ]
        widgets = {
            'first_name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombre'}),
            'last_name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Apellido'}),
            'username': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombre de usuario'})
        }

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.es_medico = True
        user.save()
        # student = Student.objects.create(user=user)
        # student.interests.add(*self.cleaned_data.get('interests'))
        return user
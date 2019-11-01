from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from administracion.models import Medico, Paciente
from .forms import FormularioMedico
from django.contrib.auth import login

@login_required(login_url='/')
def index(request):
    return render(request, 'index.html')

def mostrar_login(request):
    return render(request, 'login.html')

def user_logout(request):
    logout(request)
    return redirect('/')

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/index')
        else:
            messages.error(request, "El usuario o la contraseña son incorrectos.")
            return redirect('/')
    else:
        return redirect('/')

class CrearCuentaMedico(CreateView):
    model = Medico
    form_class = FormularioMedico
    template_name = 'register.html'
    success_url = '/index'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/index')

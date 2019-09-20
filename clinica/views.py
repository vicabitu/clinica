from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

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

def crear_cuenta(request):
    return render(request, 'register.html')

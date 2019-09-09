from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.urls import reverse

def index(request):
    return render(request, 'index.html')

def mostrar_login(request):
    return render(request, 'login.html')

def user_login(request):
    print('Hola')

    if request.method == 'POST':
        username = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # return HttpResponse("Login")
            return HttpResponseRedirect(reverse('index'))
        else:
            return HttpResponse("No Login")
    else:
        pass
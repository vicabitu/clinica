"""clinica URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.mostrar_login, name='mostrar_login'),
    path('index/', views.index, name='index'),
    path('user_login', views.user_login, name='user_login'),
    path('logout', views.user_logout, name='logout'),
    path('crear_cuenta_medico', views.CrearCuentaMedico.as_view(), name='crear_cuenta_medico'),
    path('crear_cuenta_paciente', views.CrearCuentaPaciente.as_view(), name='crear_cuenta_paciente'),
    path('elegir_tipo_de_cuenta', views.elegir_tipo_de_cuenta, name='elegir_tipo_de_cuenta')
]

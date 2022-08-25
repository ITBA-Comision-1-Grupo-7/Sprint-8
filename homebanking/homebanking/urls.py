"""homebanking URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from login import views as login_views
from django.conf import settings
from django.conf.urls.static import static
from tarjetas import views as tarjetas_views
from prestamos import views as prestamo_views
from cuentas import views as cuentas_views
from django.urls import include
from cuentas import views 
from django.contrib.auth import views as views_de_jaqueo
from api import views as api_views
from clientes import views as cliente_views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views_de_jaqueo.LoginView.as_view()),
    path('tarjetas/', tarjetas_views.Tarjeta, name="tarjetas"),
    path('prestamos/', prestamo_views.prestamo, name="prestamos"),
    path('accounts/',include('django.contrib.auth.urls')),
    path('registro/',login_views.registro, name="registro"),
    path('cuentas/', views.Cuenta, name= "cuentas"),
    path('api/', api_views.SucursalesLists.as_view(), name= "api_sucursales"),
    path('api/<int:cliente_id>/', cliente_views.ClienteDetails.as_view(), name= "api_cliente_details"),
    path('api/prestamo/', api_views.Create_prestamo.as_view(), name= "api_create_prestamo"),



]

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
    path('api/saldo/<int:pk>/', api_views.SaldoDetails.as_view(), name="api_saldo_details"),
    # path('api/cliente/<int:customer_dni>/',api_views.TarjetasDeCliente.as_view(), name="api_cliente_tarjetas"),
    # path('api/cliente/direccion/<int:customer_dni>/',api_views.CambiarDireccionCliente.as_view(), name="api_cliente_direccion"),
]

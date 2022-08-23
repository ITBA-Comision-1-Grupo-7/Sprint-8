from django.shortcuts import render, redirect
from django.urls import reverse
from .form import RegistroForm
from django.contrib.auth.models import User
##### CAMBIAR  POR HOME
def home(request):
    return render(request, "login/home.html")




def registro(request):
    registro_form = RegistroForm

    if request.method == "POST":
        registro_form = registro_form(data=request.POST)
        cliente_id= request.POST.get('cliente_id','')
        email = request.POST.get('email','')
        pwd = request.POST.get('pwd','')
        print(cliente_id,email,pwd)
        user = User.objects.create_user(cliente_id, email, pwd)
        user.save()
        print('creado')
        return redirect(reverse('login'))
    return render(request,"login/registro.html",{'form': registro_form})

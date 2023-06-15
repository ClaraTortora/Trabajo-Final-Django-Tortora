from django.shortcuts import render

#Importaciones para el login y el registro
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from . import forms



# Create your views here.
def index(request):
    return render (request, 'home/index.html')

#LOGIN
def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request.POST, data=request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contraseña = form.cleaned_data.get('password')
            user = authenticate(username=usuario, password=contraseña)
            if user is not None:
                login(request, user)
                return render(request, 'home/index.html', {'mensaje':f'¡Bienvenid@ {usuario}!'})
    else:
        form = AuthenticationForm()
    return render(request, 'home/login.html', {'form': form})


#REGISTRO
def register(request):
    if request.method == "POST":
        form = forms.CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'home/index.html', {'mensaje':'¡Usuario creado con éxito!'})
    else:
        form = forms.CustomUserCreationForm()
    return render(request, 'home/register.html', {'form': form})


#SOBRE MI 
def aboutme(request):
    return render(request, 'home/aboutme.html')
    
          
           
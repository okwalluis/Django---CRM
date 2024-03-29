from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm
from base.personas.models import Persona, TipoPersona, Sexo

def home(request):
    personas = Persona.objects.all()
	# Check to see if logging in
    if request.method == 'POST':
        username = request.POST.get('username','')
        password = request.POST.get('password','')
		# Authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Bienvenido!")
            return redirect('home:home')
        else:
            messages.success(request, "Ha ocurrido un error!")
            return redirect('home:home')
    else:
        return render(request, 'home.html', {'personas':personas})

def logout_user(request):
    logout(request)
    messages.success(request, 'Te has desconectado!')
    return redirect('home:home')

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Authenticate and login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password= password)
            login(request, user)
            messages.success(request, "Te has registrado con exito!")
            return redirect('home:home')
    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form':form})
    
    return render(request, 'register.html', {'form':form})
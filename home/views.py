
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm
from personas.models import Persona, TipoPersona, Sexo

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

#def login_user(request):
#    pass

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
"""
def persona_record(request, pk):
    if request.user.is_authenticated:
        # Look Up Record
        persona_record = Persona.objects.get(id=pk)
        
        if persona_record.sexo is not None:
            sexo = persona_record.sexo.descripcion
        else:
            sexo = ''
        
        if persona_record.tipo_persona is not None:
            tipo = persona_record.tipo_persona.descripcion
        else:
            tipo = ''
            
        return render(request, 'persona_record.html', {'persona_record':persona_record, 'tipo':tipo, 'sexo':sexo})
    else:
        messages.success(request, "Debes conectarte para visualizar la información")
        return redirect('home:home')

def delete_record(request, pk):
    if request.user.is_authenticated:
        delete_it = Persona.objects.get(id=pk)
        delete_it.delete()
        messages.success(request, "El registro fue borrado con éxito.")
        return redirect('home:home')
    else:
        messages.success(request, "Debes estar conectado.")
        return redirect('home:home')

def add_record(request):
    if request.user.is_authenticated:
        return render(request, 'add_record.html', {})
    else:
        messages.success(request, "Debes estar conectado.")
        return redirect('home:home')
"""        
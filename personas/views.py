from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Persona
from .forms import PersonaForm

# Personas
def listar_personas(request):
    if request.user.is_authenticated:
        personas = Persona.objects.all()
        return render(request, 'lista_personas.html', {'personas': personas})
    else:
        messages.success(request, "Debes conectarte para visualizar la información")
        return redirect('home:home')

def listar_persona_por_id(request, pk):
    if request.user.is_authenticated:
        # Look Up Record
        persona = get_object_or_404(Persona, id=pk)
        if persona.sexo is not None:
            sexo = persona.sexo.descripcion
        else:
            sexo = ''
        if persona.tipo_persona is not None:
            tipo = persona.tipo_persona.descripcion
        else:
            tipo = ''
        return render(request, 'persona.html', {'persona':persona, 'tipo':tipo, 'sexo':sexo})
    else:
        messages.success(request, "Debes conectarte para visualizar la información")
        return redirect('home:home')

def agregar_persona(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PersonaForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Registro insertado con éxito!")
                return redirect('personas:listar_personas')
        else:
            form = PersonaForm()
        
        return render(request, 'agregar_persona.html', {'form': form})
    else:
        messages.success(request, "Debes estar conectado.")
        return redirect('home:home')

def borrar_persona(request, pk):
    if request.user.is_authenticated:
        delete_it = get_object_or_404(Persona, id=pk)
        delete_it.delete()
        messages.success(request, "El registro fue borrado con éxito.")
        return redirect('personas:listar_personas')
    else:
        messages.success(request, "Debes estar conectado.")
        return redirect('home:home')

def editar_persona(request, pk):
    if request.user.is_authenticated:
        persona = get_object_or_404(Persona, id=pk)
        form = PersonaForm(request.POST or None, instance=persona)
        if form.is_valid():
            form.save()
            messages.success(request, "El registro fue editado con éxito.")
            return redirect('personas:listar_personas')
        return render(request, 'editar_persona.html', {'form': form})
    else:
        messages.success(request, "Debes estar conectado.")
        return redirect('home:home')

## 
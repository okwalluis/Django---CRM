from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.db import models

from .models import Persona, Direccion, Telefono, Documento, TipoDocumento
from .forms import PersonaForm, DireccionForm, TelefonoForm, DocumentoForm

# Personas
def listar_personas(request):
    if request.user.is_authenticated:
        personas = Persona.objects.all()
        return render(request, 'lista_personas.html', {'personas': personas})
    else:
        messages.success(request, "Debes conectarte para visualizar la información")
        return redirect('home:home')

def listar_persona_string(request, string):
    if request.user.is_authenticated:
        if string:
            personas = Persona.objects.filter(
                models.Q(nombre__icontains=string) |
                models.Q(apellido__icontains=string) |
                models.Q(razon_social__icontains=string)
            )
            return render(request, 'lista_personas.html', {'personas': personas})
        else:
            return redirect('personas:listar_personas')
    else:
        messages.success(request, "Debes conectarte para visualizar la información")
        return redirect('home:home')

def listar_persona_por_id(request, pk):
    if request.user.is_authenticated:
        persona = get_object_or_404(Persona, id=pk)
        direcciones = Direccion.objects.filter(persona=persona)
        documentos = Documento.objects.filter(persona=persona)
        telefonos = Telefono.objects.filter(persona=persona)

        if persona.sexo is not None:
            sexo = persona.sexo.descripcion
        else:
            sexo = ''
        if persona.tipo_persona is not None:
            tipo = persona.tipo_persona.descripcion
        else:
            tipo = ''
        
        direccion_form = DireccionForm(initial={'persona': persona},persona=persona)
        documento_form = DocumentoForm(initial={'persona': persona},persona=persona)
        telefono_form = TelefonoForm(initial={'persona': persona}, persona=persona)
            
        if request.method == 'POST':
            if 'direccion_form_submit' in request.POST:
                direccion_form = DireccionForm(request.POST, persona=persona)
                if direccion_form.is_valid():
                    direccion = direccion_form.save(commit=False)
                    direccion.persona = persona
                    direccion.save()
                    messages.success(request, "Dirección registrada con éxito.")
                    return redirect('personas:listar_persona_por_id', pk=pk)
            elif 'documento_form_submit' in request.POST:
                documento_form = DocumentoForm(request.POST, persona=persona)
                if documento_form.is_valid():
                    documento = documento_form.save(commit=False)
                    documento.persona = persona
                    documento.save()
                    messages.success(request, "Documento registrado con éxito.")
                    return redirect('personas:listar_persona_por_id', pk=pk)
            elif 'telefono_form_submit' in request.POST:
                telefono_form = TelefonoForm(request.POST)
                if telefono_form.is_valid():
                    telefono = telefono_form.save(commit=False)
                    telefono.persona = persona
                    telefono.save()
                    messages.success(request, "Teléfono registrado con éxito.")
                    return redirect('personas:listar_persona_por_id', pk=pk)
            
        return render(request, 'persona.html', {
            'persona': persona,
            'direcciones': direcciones,
            'documentos': documentos,
            'telefonos': telefonos,
            'tipo': tipo,
            'sexo': sexo,
            'direccion_form': direccion_form,
            'documento_form': documento_form,
            'telefono_form': telefono_form
        })
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

##  direcciones
def borrar_direccion(request, pk):
    if request.user.is_authenticated:
        delete_it = get_object_or_404(Direccion, id=pk)
        persona = delete_it.persona
        delete_it.delete()
        messages.success(request, "El registro fue borrado con éxito.")
        return redirect('personas:listar_persona_por_id', pk=persona.id)
    else:
        messages.success(request, "Debes estar conectado.")
        return redirect('home:home')

def listar_direcciones(request, pk):
    if request.user.is_authenticated:
        persona = get_object_or_404(Persona, id=pk)
        direcciones = Direccion.objects.filter(persona=persona)
        return render(request, 'lista_direcciones.html', {'persona': persona, 'direcciones': direcciones})
    else:
        messages.success(request, "Debes conectarte para visualizar la información")
        return redirect('home:home')
    
##  documentos
def borrar_documento(request, pk):
    if request.user.is_authenticated:
        delete_it = get_object_or_404(Documento, id=pk)
        persona = delete_it.persona
        delete_it.delete()
        messages.success(request, "El registro fue borrado con éxito.")
        return redirect('personas:listar_persona_por_id', pk=persona.id)
    else:
        messages.success(request, "Debes estar conectado.")
        return redirect('home:home')

def listar_documentos(request, pk):
    if request.user.is_authenticated:
        persona = get_object_or_404(Persona, id=pk)
        documentos = Documento.objects.filter(persona=persona)
        return render(request, 'lista_documentos.html', {'persona': persona, 'documentos': documentos})
    else:
        messages.success(request, "Debes conectarte para visualizar la información")
        return redirect('home:home')
##  telefonos
def borrar_telefono(request, pk):
    if request.user.is_authenticated:
        delete_it = get_object_or_404(Telefono, id=pk)
        persona = delete_it.persona
        delete_it.delete()
        messages.success(request, "El registro fue borrado con éxito.")
        return redirect('personas:listar_persona_por_id', pk=persona.id)
    else:
        messages.success(request, "Debes estar conectado.")
        return redirect('home:home')

def listar_telefonos(request, pk):
    if request.user.is_authenticated:
        persona = get_object_or_404(Persona, id=pk)
        telefonos = Telefono.objects.filter(persona=persona)
        return render(request, 'lista_telefonos.html', {'persona': persona, 'telefonos': telefonos})
    else:
        messages.success(request, "Debes conectarte para visualizar la información")
        return redirect('home:home')
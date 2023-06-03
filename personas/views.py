from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Persona, TipoPersona, Sexo


class PersonaView(View):
    def get(self, request):
        personas = Persona.objects.all()
        return render(request, 'personas/persona.html', {'personas': personas})


def nuevo(request):
    tipos = TipoPersona.objects.all()
    sexos = Sexo.objects.all()

    return render(
        request,
        template_name='personas/nuevo.html',
        context={'titulo': 'Nuevo',
                 'tipos': tipos,
                 'lblsexo': 'Sexo',
                 'sexos': sexos}
    )


def cancelar(request):
    personas = Persona.objects.all()
    return render(request, 'personas/persona.html', {'personas': personas})


def borrar(request, pk):
    persona = get_object_or_404(Persona, id=pk)
    persona.delete()
    return redirect('persona:personas')


def crear(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        razon_social = request.POST.get('razonsocial')

        # Suponiendo que 'tipo_persona' es el nombre del campo en el formulario
        tipo_persona_id = request.POST.get('tipopersona')
        tipo_persona = get_object_or_404(TipoPersona, id=tipo_persona_id)

        sexo_id = request.POST.get('sexo')
        sexo = get_object_or_404(Sexo, id=sexo_id)

        es_cliente = 'escliente' in request.POST
        es_proveedor = 'esproveedor' in request.POST

        persona = Persona(nombre=nombre,
                          apellido=apellido,
                          razon_social=razon_social,
                          tipo_persona=tipo_persona,
                          sexo=sexo,
                          es_cliente=es_cliente,
                          es_proveedor=es_proveedor)
        persona.save()
        # Redirige a la página que muestra la lista de personas
        return redirect('persona:personas')

    return render(request, 'personas/persona.html')

from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import Prestamo, CuotaPrestamo
from .forms import PrestamoForm, PrestamoEditarForm

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def listar_prestamos(request):
    if request.user.is_authenticated:
        prestamos = Prestamo.objects.all().order_by('-fecha')
        return render(request, 'lista_prestamos.html', {'prestamos': prestamos})
    else:
        messages.success(request, "Debes conectarte para visualizar la información")
        return redirect('home:home')

def listar_prestamo_por_id(request, pk):
    if request.user.is_authenticated:
        # Look Up Record
        prestamo = get_object_or_404(Prestamo, id=pk)
        if prestamo.sistema_prestamo is not None:
            sistema_prestamo = prestamo.sistema_prestamo.descripcion
        else:
            sexo = ''

        if prestamo.tipo_prestamo is not None:
            tipo_prestamo = prestamo.tipo_prestamo.descripcion
        else:
            tipo_prestamo = ''

        if prestamo.frecuencia is not None:
            frecuencia = prestamo.frecuencia.descripcion
        else:
            frecuencia = ''

        if prestamo.estado_prestamo is not None:
            estado_prestamo = prestamo.estado_prestamo.descripcion
        else:
            estado_prestamo = ''
            
        return render(request, 'prestamo.html', {'prestamo':prestamo })
    else:
        messages.success(request, "Debes conectarte para visualizar la información")
        return redirect('home:home')

def agregar_prestamo(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PrestamoForm(request.POST, user=request.user)
            if form.is_valid():
                prestamo = form.save(commit=False)
                # aqui podemos asignar los valores por defecto
                prestamo.created_by = request.user
                prestamo.save()

                ##form.save()
                #prestamo = form.save()
                #prestamo_id = prestamo.id
                
                messages.success(request, "Registro insertado con éxito!")
                # crear cuotas del último prestamo registrado
                return redirect('prestamos:listar_prestamos')
        else:
            form = PrestamoForm()
        
        return render(request, 'agregar_prestamo.html', {'form': form})
    else:
        messages.success(request, "Debes estar conectado.")
        return redirect('home:home')

def editar_prestamo(request, pk):
    if request.user.is_authenticated:
        prestamo = get_object_or_404(Prestamo, id=pk)
        form = PrestamoEditarForm(request.POST or None, instance=prestamo)
        if form.is_valid():
            form.save()
            messages.success(request, "El registro fue editado con éxito.")
            return redirect('prestamos:listar_prestamos')
        return render(request, 'editar_prestamo.html', {'form': form})
    else:
        messages.success(request, "Debes estar conectado.")
        return redirect('home:home')

# CUOTAS
# Aqui recupero las cuotas por prestamo y paso al template de manera a listarlas por orden de cuota.
def listar_cuotas_por_id(request, fk):
    if request.user.is_authenticated:
        # Look Up Record
        #print(fk)
        cuotas = CuotaPrestamo.objects.filter(prestamo_id=fk).order_by('nro_cuota')

        return render(request, 'lista_cuotas_prestamo.html', {'cuotas':cuotas })
    else:
        messages.success(request, "Debes conectarte para visualizar la información")
        return redirect('home:home')
# PAGARE
def generar_pagare(request, fk):
    # Crear el objeto response con el tipo de contenido PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="recibo.pdf"'

    # Crear el objeto canvas para generar el PDF
    p = canvas.Canvas(response, pagesize=letter)

    # Agregar contenido al PDF
    p.setFont("Helvetica", 12)
    p.drawString(100, 700, "Pagare")
    p.drawString(100, 680, f"Cuota: {fk}")
    # Agregar más contenido según tus necesidades

    # Finalizar y guardar el PDF
    p.showPage()
    p.save()

    return response
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.db import models

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from num2words import num2words
import locale
from django.db import connection

from .models import Prestamo, CuotaPrestamo, EstadoCuentaPrestamo
from .forms import PrestamoForm, EstadoCuentaPrestamoForm
from pagares.models import Pagare
from personas.models import Documento, Direccion

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
            sistema_prestamo = ''

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

def listar_prestamo_string(request, string):
    if request.user.is_authenticated:
        if string:
            prestamos = Prestamo.objects.filter(
                models.Q(nro_prestamo__icontains=string) #|
                #models.Q(persona__icontains=string)
            )
            return render(request, 'lista_prestamos.html', {'prestamos': prestamos})
        else:
            return redirect('prestamos:listar_prestamos')
    else:
        messages.success(request, "Debes conectarte para visualizar la información")
        return redirect('home:home')

def agregar_prestamo(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PrestamoForm(request.POST, user=request.user, operacion='I')
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
        form = PrestamoForm(request.POST or None, instance=prestamo, operacion='E')
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

# Estado de cuenta
def reporte_estado_cuenta(request):
    if request.method == 'POST':
        form = EstadoCuentaPrestamoForm(request.POST)
        if form.is_valid():
            persona = form.cleaned_data.get('persona')
            prestamo = form.cleaned_data.get('prestamo')
            fecha_emision_desde = form.cleaned_data.get('fecha_emision_desde')
            fecha_emision_hasta = form.cleaned_data.get('fecha_emision_hasta')
            fecha_vencimiento_desde = form.cleaned_data.get('fecha_vencimiento_desde')
            fecha_vencimiento_hasta = form.cleaned_data.get('fecha_vencimiento_hasta')

            estados = EstadoCuentaPrestamo.objects.all()
            # Cliente no debe ser nulo
            if persona is not None and persona.id is not None:
                estados = estados.filter(persona_id=persona.id)
                
            if prestamo is not None and prestamo.id is not None:
                estados = estados.filter(nro_prestamo=prestamo.id)
            
            if fecha_emision_desde is not None and fecha_emision_hasta is not None:
                estados = estados.filter(fecha__range=(fecha_emision_desde, fecha_emision_hasta))
            
            if fecha_vencimiento_desde is not None and fecha_vencimiento_hasta is not None:
                #estados = estados.filter(fecha_vencimiento__range=(fecha_vencimiento_desde, fecha_vencimiento_hasta))
                estados = estados.filter(fecha_vencimiento__gte=fecha_vencimiento_desde, fecha_vencimiento__lte=fecha_vencimiento_hasta)
                
            # Otras operaciones para generar el informe...
            return render(request, 'informe_estado_cuenta.html', {'persona':persona, 'estados': estados})
    else:
        form = EstadoCuentaPrestamoForm()
    
    return render(request, 'consultar_estado_cuenta.html', {'form':form})

def imprimir_pagare(request, pagare):
#    fecha_vencimiento = cuota.fecha_vencimiento
    try:
        # Intenta obtener el objeto Pagare que coincida con la cuota de préstamo
        documento_deudor = Documento.objects.get(persona_id=pagare.persona_id) # tipo 1 CEDULA
    except Pagare.DoesNotExist:
        documento_deudor = ''
    try:
        # Intenta obtener el objeto Pagare que coincida con la cuota de préstamo
        direccion_deudor = Direccion.objects.get(persona_id=pagare.persona_id, por_defecto=True)
    except Pagare.DoesNotExist:
        direccion_deudor = ''

    # Crear el objeto response con el tipo de contenido PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="pagare_{pagare.persona}_{pagare.id}.pdf"'

    w, h = A4
    # Crear el objeto canvas para generar el PDF
    #p = canvas.Canvas(response, pagesize=letter)
    p = canvas.Canvas(response, pagesize=A4)
    # Estilo del documento
    p.setFont("Helvetica-Bold", 12)
        
    
    y = 60 # y inicial
    x = 40 # x inicial
    # Nro pagaré
    p.drawString(x + 25, h-y, "N°")
    p.setFont("Helvetica-Bold", 12)
    p.drawString(235, h-y, "PAGARÉ A LA ORDEN")
    p.drawString(460, h-y, "IMPORTE")

    y = y + 6
    # Cuadro nro. pagaré
    p.rect(x, h - y, 60, 20)
    # Cuadro importe
    p.rect(x+400, h - y, 90, 20)

    y = y + 20
    p.setFont("Helvetica", 12)
    # DATOS
    # Nro. pagare
    p.drawString(x + 27, h-y, f"{pagare.id}")

    # Vencimiento
    p.drawString(240, h - y, "Vence")
    p.drawString(292, h - y, str(pagare.fecha_vencimiento.day))
    p.drawString(314, h - y, str(pagare.fecha_vencimiento.month))
    p.drawString(334, h - y, str(pagare.fecha_vencimiento.year))
    # Importe
    p.drawString(450, h - y, "Gs.")
    p.drawString(473, h - y, str("{:,.0f}".format(pagare.monto_pagare).replace(",", ".")))
    
    y = y + 6
    #Cuadro nro. pagaré 2
    p.rect(x, h - y, 60, 26)
    # Cuadro importe 2
    p.rect(440, h - y, 90, 26)
    
    # Cuadros Vence
    p.rect(290, h - y, 20, 20)
    p.rect(310, h - y, 20, 20)
    p.rect(330, h - y, 40, 20)
    

    p.setFont("Helvetica", 12)
    y = y + 36
    locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')
    p.drawRightString(x + 485, h - y, f"PJC, {str(pagare.fecha_emision.day)} de {pagare.fecha_emision.strftime('%B')} de {str(pagare.fecha_emision.year)}")

    texto = f"Por este pagaré a la orden me/nos obliga/mos a pagar el día {str(pagare.fecha_vencimiento.day)} de "\
            f"{pagare.fecha_vencimiento.strftime('%B')} de {str(pagare.fecha_vencimiento.year)} a "\
            "JOSÉ ANTONIO OLMEDO KISCHKEL o a su orden, en su local de calle Jorge Groessinger, "\
            "Barrio Terrazas I, de la ciudad de Pedro Juan Caballero la suma de Guaraníes: "\
            f"{num2words(pagare.monto_pagare, lang='es')} "\
            "por igual valor recibido en dinero/efectivo a mi/nuestra satisfacción."

    # Dividir el texto en líneas de 90 caracteres sin cortar palabras
    palabras = texto.split()
    lineas = []
    linea_actual = ""
    for palabra in palabras:
        if len(linea_actual + palabra) <= 90:
            linea_actual += palabra + " "
        else:
            lineas.append(linea_actual.strip())
            linea_actual = palabra + " "
    lineas.append(linea_actual.strip())

    for linea in lineas:
        y = y + 30
        p.drawString(x, h - y, linea)
    
    y = y + 50
    p.drawString(x, h - y, f"-----------------------------------")
    p.drawString(x + 300, h - y, f"-----------------------------------")
    y = y + 10
    p.drawString(x, h - y, f"Firma Co-Deudor:")
    p.drawString(x + 300, h - y, f"Firma Deudor:")
    y = y + 20    
    p.drawString(x + 300, h - y, f"{pagare.persona.nombre} {pagare.persona.apellido}")
    y = y + 20
    p.drawString(x, h - y, f"Documento: ")
    p.drawString(x + 300, h - y, f"Documento: {documento_deudor.numero}" )
    y = y + 20
    p.drawString(x, h - y, f"Dirección: ")
    p.drawString(x + 300, h - y, f"Dirección: {direccion_deudor.descripcion}" )

    p.drawString(x, h/2, "_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")

    # Finalizar y guardar el PDF
    p.showPage()
    p.save()

    return response

# PAGARE
def generar_pagare(request, fk):
    cuota = get_object_or_404(CuotaPrestamo, id=fk)
    try:
        # Intenta obtener el objeto Pagare que coincida con la cuota de préstamo
        pagare = Pagare.objects.get(cuota_id=cuota.id)
    except Pagare.DoesNotExist:
        # Si no se encuentra un Pagare, ejecuta el procedimiento para generarlo
        with connection.cursor() as cursor:
            cursor.execute('CALL pa_generar_pagare(%s)', [cuota.id])
        try:
            pagare = Pagare.objects.get(cuota_id=cuota.id)
        except Pagare.DoesNotExist:
            # Si aún no se encuentra un Pagare después de ejecutar el procedimiento, puedes manejarlo aquí
            # Por ejemplo, puedes mostrar un mensaje de error o redirigir a otra página
            return HttpResponse("Error: No se pudo generar el Pagare.")
        
    return imprimir_pagare(request, pagare)
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib import messages
from django.db import IntegrityError

from .forms import PagoForm 
from prestamos.models import CuotaPrestamo

def pagar_cuota_por_id(request, fk):
    if request.user.is_authenticated:
        cuota = get_object_or_404(CuotaPrestamo, id=fk)
        cuotas = CuotaPrestamo.objects.filter(prestamo_id=fk).order_by('nro_cuota')
        #form = PagoForm(request.POST or None, instance=cuota)
        form = PagoForm(request.POST or None, initial={'cuota':cuota,'monto_pago': cuota.saldo_cuota})
        try:
            if form.is_valid():
                form.save()
                messages.success(request, "El pago fue realizado con éxito.")
                return redirect(reverse('prestamos:listar_cuotas_por_id', kwargs={'fk': cuota.prestamo_id}), cuotas=cuotas)
        except IntegrityError:
            messages.error(request, "El pago no debe ser superior al saldo de la cuota.")
        return render(request, 'agregar_pago.html', {'form': form, 'cuota':cuota})
    else:
        messages.success(request, "Debes estar conectado.", extra_tags='alert-message')
        return redirect('home:home')
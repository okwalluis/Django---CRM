from django.db import models
from base.suscripciones.models import Suscripcion

class HistorialPago(models.Model):
    suscripcion = models.ForeignKey(Suscripcion, on_delete=models.PROTECT, null=True)
    monto = models.DecimalField(max_digits=12, decimal_places=0)
    fecha_pago = models.DateField()
    
    class Meta:
        db_table = 'historial_pagos'
from django.db import models
from prestamos.models import CuotaPrestamo
from personas.models import Persona

class Pagare(models.Model):
    cuota = models.ForeignKey(CuotaPrestamo, on_delete=models.PROTECT)
    monto_pagare = models.DecimalField(max_digits=12, decimal_places=0)
    fecha_emision = models.DateField()
    fecha_vencimiento = models.DateField()
    persona = models.ForeignKey(Persona, on_delete=models.PROTECT)
    nombre_co_deudor = models.CharField(max_length=100, null=True)
    documento_co_deudor = models.CharField(max_length=20, null=True)
    direccion_co_deudor = models.CharField(max_length=100, null=True)
    
    def __str__(self):
        return f'Pagaré: {self.id}. - {self.cuota}'

    class Meta:
        db_table = 'pagares'
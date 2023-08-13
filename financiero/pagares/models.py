from django.db import models
from financiero.prestamos.models import CuotaPrestamo
from base.personas.models import Persona
from base.empresas.models import Empresa

class Pagare(models.Model):
    cuota = models.ForeignKey(CuotaPrestamo, on_delete=models.PROTECT)
    monto_pagare = models.DecimalField(max_digits=12, decimal_places=0)
    fecha_emision = models.DateField()
    fecha_vencimiento = models.DateField()
    persona = models.ForeignKey(Persona, on_delete=models.PROTECT)
    nombre_co_deudor = models.CharField(max_length=100, null=True)
    documento_co_deudor = models.CharField(max_length=20, null=True)
    direccion_co_deudor = models.CharField(max_length=100, null=True)
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT, null=True)
    
    def __str__(self):
        return f'Pagaré: {self.id}. - {self.cuota}'

    class Meta:
        db_table = 'pagares'
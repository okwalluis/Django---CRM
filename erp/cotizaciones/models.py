from django.db import models
from base.empresas.models import Empresa
from erp.monedas.models import Moneda
from enum import Enum

class TipoCambio(Enum):
    COMPRA = 'Compra'
    VENTA = 'Venta'

class Cotizacion(models.Model):
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT)
    fecha = models.DateField()
    moneda = models.ForeignKey(Moneda, on_delete=models.PROTECT)
    tipo_cambio = models.CharField(
        max_length=20,
        choices=[(tipo_cambio.value, tipo_cambio.name) for tipo_cambio in TipoCambio]
    )
    valor = models.FloatField()
    
    class Meta:
        db_table = 'cotizaciones'

    def __str__(self):
        return f'{self.fecha} - {self.moneda} - {self.valor}'

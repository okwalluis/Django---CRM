from django.db import models
from base.empresas.models import Empresa
from control_stock.operaciones_stock.models import OperacionStock
from enum import Enum
from erp.tipos_comprobantes.models import TipoComprobante

class Saldo(Enum):
    NINGUNO = 'No afecta'
    DEBE = 'Débito'
    HABER = 'Crédito'

class TipoMovimiento(models.Model):
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT)
    descripcion = models.CharField(max_length=50)
    operacion = models.ForeignKey(OperacionStock, on_delete=models.PROTECT)
    afecta_saldo = models.CharField(
        max_length=20,
        choices=[(afecta_saldo.value, afecta_saldo.name) for afecta_saldo in Saldo]
    )
    tipo_comprobante = models.ForeignKey(TipoComprobante, on_delete=models.PROTECT)
    
    class Meta:
        db_table = 'tipos_movimientos'
    
    def __str__(self):
        return f'{self.descripcion}'
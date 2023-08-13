from django.db import models
from base.personas.models import Persona
from base.empresas.models import Empresa
from base.sucursales.models import Sucursal
from erp.monedas.models import Moneda
from erp.tipos_movimientos.models import TipoMovimiento

class Movimiento(models.Model):
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT)
    sucursal = models.ForeignKey(Sucursal, on_delete=models.PROTECT)
    tipo_movimiento = models.ForeignKey(TipoMovimiento, on_delete=models.PROTECT)
    fecha = models.DateField()
    nro_documento = models.CharField(max_length=20)
    moneda = models.ForeignKey(Moneda, on_delete=models.PROTECT)
    cuenta = models.ForeignKey(Persona, on_delete=models.PROTECT)
    monto_total = models.FloatField()
    monto_grav10 = models.FloatField()
    monto_grav5 = models.FloatField()
    monto_iva10 = models.FloatField()
    monto_iva5 = models.FloatField()
    monto_exento = models.FloatField()
    tasa_cambio = models.FloatField()
    
    class Meta:
        db_table = 'movimientos'
    
    def __str__(self):
        return self.sigla
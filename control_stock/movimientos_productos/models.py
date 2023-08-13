from django.db import models
from control_stock.productos.models import Producto
from control_stock.depositos.models import Deposito
from control_stock.lotes.models import Lote
from base.empresas.models import Empresa

class MovimientoProducto(models.Model):
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT)
    deposito = models.ForeignKey(Deposito, on_delete=models.PROTECT)
    producto = models.ForeignKey(Producto, on_delete=models.PROTECT)
    fecha = models.DateField()
    saldo_anterior = models.FloatField()
    cantidad_entrada = models.FloatField()
    cantidad_salida = models.FloatField()
    saldo_actual = models.FloatField()

    class Meta:
        db_table = 'movimientos_productos'
    
class MovimientoProductoLote(models.Model):
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT)
    deposito = models.ForeignKey(Deposito,on_delete=models.PROTECT)
    producto = models.ForeignKey(Producto, on_delete=models.PROTECT)
    lote = models.ForeignKey(Lote, on_delete=models.PROTECT)
    fecha = models.DateField()
    saldo_anterior = models.FloatField()
    cantidad_entrada = models.FloatField()
    cantidad_salida = models.FloatField()
    saldo_actual = models.FloatField()

    class Meta:
        db_table = 'movimientos_productos_lotes'
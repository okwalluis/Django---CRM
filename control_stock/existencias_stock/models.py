from django.db import models
from control_stock.depositos.models import Deposito
from control_stock.lotes.models import Lote
from control_stock.productos.models import Producto

from base.empresas.models import Empresa
from base.sucursales.models import Sucursal

"""
    El objetivo es controlar la existencia de un producto por lote en un cierto deposito.
    Se asume que todos los productos nacen con un lote, por mas que este sea generico.
"""
"""
    En el primer caso controlamos existencia del producto, por lote, por deposito
"""
class ExistenciaProductoLote(models.Model):
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT)
    sucursal = models.ForeignKey(Sucursal, on_delete=models.PROTECT)
    deposito = models.ForeignKey(Deposito, on_delete=models.PROTECT)
    producto = models.ForeignKey(Producto, on_delete=models.PROTECT)
    lote = models.ForeignKey(Lote, on_delete=models.PROTECT)
    saldo_anterior = models.FloatField()
    cantidad_entrada = models.FloatField()
    cantidad_salida = models.FloatField()
    saldo_actual = models.FloatField()
    
    class Meta:
        db_table = 'existencias_productos_lotes'

    def __str__(self):
        return f'{self.producto} /{self.lote}:{self.saldo_actual}'

"""
    En el segundo caso controlamos existencia del producto por deposito y calculamos el costo promedio
"""

class ExistenciaProducto(models.Model):
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT)
    producto = models.ForeignKey(Producto, on_delete=models.PROTECT)
    deposito = models.ForeignKey(Deposito, on_delete=models.PROTECT)
    saldo_anterior = models.FloatField()
    cantidad_entrada = models.FloatField()
    cantidad_salida = models.FloatField()
    saldo_actual = models.FloatField()
    costo_medio = models.FloatField()
    costo_medio_ponderado = models.FloatField()
    
    class Meta:
        db_table = 'existencias_productos'

    def __str__(self):
        return f'{self.producto}: {self.saldo_actual}'
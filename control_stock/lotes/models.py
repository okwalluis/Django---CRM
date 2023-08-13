from django.db import models
from control_stock.productos.models import Producto
from base.empresas.models import Empresa

class Lote(models.Model):
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT)    
    producto = models.ForeignKey(Producto, on_delete=models.PROTECT)
    nro_lote = models.CharField(max_length=30, default='0000')
    fecha_elaboracion = models.DateField()
    fecha_vencimiento = models.DateField()
    descripcion = models.CharField(max_length=50, unique=True)
    activo = models.BooleanField(default=True)

    class Meta:
        db_table = 'lotes'

    def __str__(self):
        return f'{self.producto}/{self.nro_lote}'
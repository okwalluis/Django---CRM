from django.db import models
from control_stock.familias.models import FamiliaProducto
from control_stock.grupos.models import GrupoProducto
from control_stock.clases_productos.models import ClaseProducto
from control_stock.tipos_productos.models import TipoProducto
from control_stock.unidades_medidas.models import UnidadMedida
from erp.impuestos.models import Impuesto
from base.empresas.models import Empresa

class Producto(models.Model):
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT)
    descripcion = models.CharField(max_length=80)
    familia = models.ForeignKey(FamiliaProducto, on_delete=models.PROTECT)
    grupo = models.ForeignKey(GrupoProducto, on_delete=models.PROTECT)
    impuesto = models.ForeignKey(Impuesto, on_delete=models.PROTECT)
    clase = models.ForeignKey(ClaseProducto, on_delete=models.PROTECT)
    tipo = models.ForeignKey(TipoProducto, on_delete=models.PROTECT)
    controla_lote = models.BooleanField(default=False)
    controla_existencia = models.BooleanField(default=True)
    unidad_medida = models.ForeignKey(UnidadMedida, on_delete=models.PROTECT)
    codigo_fabrica = models.CharField(max_length=30, null=True)
    codigo_barra = models.CharField(max_length=30, null=True)
    activo = models.BooleanField(default=True)

    class Meta:
        db_table = 'productos'

    def __str__(self):
        return self.descripcion
from django.db import models
from control_stock.familias.models import FamiliaProducto
from base.empresas.models import Empresa

class GrupoProducto(models.Model):
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT)
    descripcion = models.CharField(max_length=50, unique=True)
    familia = models.ForeignKey(FamiliaProducto, on_delete=models.PROTECT)
    activo = models.BooleanField(default=True)

    class Meta:
        db_table = 'grupos_productos'

    def __str__(self):
        return f'{self.familia.descripcion}/{self.descripcion}'
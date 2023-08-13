from django.db import models
from base.sucursales.models import Sucursal
from base.empresas.models import Empresa

class Deposito(models.Model):
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT)
    sucursal = models.ForeignKey(Sucursal, on_delete=models.PROTECT)
    descripcion = models.CharField(max_length=80)
    es_virtual = models.BooleanField(default=False)
    activo = models.BooleanField(default=True)
    
    class Meta:
        db_table = 'depositos'

    def __str__(self):
        return self.descripcion
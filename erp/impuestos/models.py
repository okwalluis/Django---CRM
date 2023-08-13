from django.db import models
from base.empresas.models import Empresa

class Impuesto(models.Model):
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT)
    descripcion = models.CharField(max_length=50)
    porcentaje = models.FloatField()
    base_imponible = models.FloatField()
    base_impuesto_incluido = models.BooleanField(default=True)
    
    class Meta:
        db_table = 'impuestos'

    def __str__(self):
        return f'{self.descripcion}'

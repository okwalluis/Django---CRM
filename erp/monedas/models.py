from django.db import models
from base.empresas.models import Empresa

class Moneda(models.Model):
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT)
    descripcion = models.CharField(max_length=50)
    sigla = models.CharField(10)
    
    class Meta:
        db_table = 'monedas'
    
    def __str__(self):
        return self.sigla
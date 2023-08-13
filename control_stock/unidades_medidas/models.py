from django.db import models
from base.empresas.models import Empresa

class UnidadMedida(models.Model):
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT)
    descripcion = models.CharField(max_length=50, unique=True)
    sigla = models.CharField(max_length=10)
    activo = models.BooleanField(default=True)
    
    class Meta:
        db_table = 'unidades_medidas'

    def __str__(self):
        return f'{self.sigla}'
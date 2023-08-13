from django.db import models
from enum import Enum

from base.empresas.models import Empresa

class Tipo(Enum):
    EMITIDO = 'Emitido'
    RECIBIDO = 'Recibido'

class TipoComprobante(models.Model):
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT)
    descripcion = models.CharField(max_length=50)
    tipo = models.CharField(
        max_length=10,
        choices=[(tipo.value, tipo.name) for tipo in Tipo]
    )

    class Meta:
        db_table = 'tipos_comprobantes'
    
    def __str__(self):
        return f'{self.descripcion} - {self.tipo}'
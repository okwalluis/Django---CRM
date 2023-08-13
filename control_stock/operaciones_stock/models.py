from django.db import models
from enum import Enum
from base.empresas.models import Empresa

"""
Toda operacion de stock obviamente afecta stock, por lo que las operaciones de stock
deben ser referenciadas en los movimientos. Caso estos afecten stock, deben referenciar a una operacion.
"""
class Operador(Enum):
    ENTRADA = 'Entrada'
    SALIDA = 'Salida'

class OperacionStock(models.Model):
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT)
    descripcion = models.CharField(max_length=50, unique=True)
    operacion = models.CharField(
        max_length=20,
        choices=[(operacion.value, operacion.name) for operacion in Operador]
    )
    activo = models.BooleanField(default=True)
    
    class Meta:
        db_table = 'operaciones_stock'

    def __str__(self):
        return f'{self.descripcion}'
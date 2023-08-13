from django.db import models
from base.empresas.models import Empresa
"""
El objetivo del tipo de producto es saber si el mismo es; adquirido, para uso o reventa; elaborado, caso de produccion.
Por defecto debe ser adquirido para su reventa, consumo, o como insumo.
"""
class TipoProducto(models.Model):
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT)
    descripcion = models.CharField(max_length=50, unique=True)
    activo = models.BooleanField(default=True)
    
    class Meta:
        db_table = 'tipos_productos'

    def __str__(self):
        return f'{self.descripcion}'
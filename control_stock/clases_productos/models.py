from django.db import models
from base.empresas.models import Empresa
"""
    La clase de producto permite distinguir entre bienes y servicios
"""
class ClaseProducto(models.Model):
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT)
    descripcion = models.CharField(max_length=80)
    activo = models.BooleanField(default=True)
    
    class Meta:
        db_table = 'clases_productos'

    def __str__(self):
        return self.descripcion
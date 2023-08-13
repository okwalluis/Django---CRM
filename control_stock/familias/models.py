from django.db import models
from base.empresas.models import Empresa

class FamiliaProducto(models.Model):
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT)
    descripcion = models.CharField(max_length=50, unique=True)
    activo = models.BooleanField(default=True)

    class Meta:
        db_table = 'familias_productos'

    def __str__(self):
        return f'{self.descripcion}'
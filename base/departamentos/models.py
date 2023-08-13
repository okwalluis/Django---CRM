from django.db import models
from base.paises.models import Pais

class Departamento(models.Model):
    descripcion = models.CharField(max_length=80)
    pais = models.ForeignKey(Pais, on_delete=models.PROTECT)
    sigla = models.CharField(max_length=5)
    activo = models.BooleanField(default=True)

    class Meta:
        db_table = 'departamentos'

    def __str__(self):
        return self.descripcion
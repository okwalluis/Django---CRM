from django.db import models
from base.departamentos.models import Departamento

class Ciudad(models.Model):
    descripcion = models.CharField(max_length=80)
    departamento = models.ForeignKey(Departamento, on_delete=models.PROTECT)
    activo = models.BooleanField(default=True)
    
    class Meta:
        db_table = 'ciudades'

    def __str__(self):
        return self.descripcion
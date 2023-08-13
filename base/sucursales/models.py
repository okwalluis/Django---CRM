from django.db import models
from base.empresas.models import Empresa
from base.paises.models import Pais
from base.departamentos.models import Departamento
from base.ciudades.models import Ciudad

class Sucursal(models.Model):
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT)
    descripcion = models.CharField(max_length=80)
    pais = models.ForeignKey(Pais, on_delete=models.PROTECT)
    departamento = models.ForeignKey(Departamento, on_delete=models.PROTECT)
    ciudad = models.ForeignKey(Ciudad, on_delete=models.PROTECT)
    direccion = models.CharField(max_length=80)
    telefono = models.CharField(max_length=20)
    activo = models.BooleanField(default=True)
    
    class Meta:
        db_table = 'sucursales'

    def __str__(self):
        return self.descripcion
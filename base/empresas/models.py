from django.db import models
from base.personas.models import Persona
from base.paises.models import Pais
from base.departamentos.models import Departamento
from base.ciudades.models import Ciudad

class Empresa(models.Model):
    descripcion = models.CharField(max_length=80)
    pais = models.ForeignKey(Pais, on_delete=models.PROTECT)
    departamento = models.ForeignKey(Departamento, on_delete=models.PROTECT)
    ciudad = models.ForeignKey(Ciudad, on_delete=models.PROTECT)
    ruc = models.CharField(max_length=20)
    representante = models.ForeignKey(Persona, on_delete=models.PROTECT)
    activo = models.BooleanField(default=True)

    class Meta:
        db_table = 'empresas'

    def __str__(self):
        return self.descripcion
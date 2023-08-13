from django.db import models
from enum import Enum
from base.empresas.models import Empresa
from control_stock.unidades_medidas.models import UnidadMedida

class Operador(Enum):
    MULTIPLICA = 'Multiplica'
    DIVIDE = 'Divide'
    POTENCIA = 'Potencia'

class ConversionMedida(models.Model):
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT)
    medida_de = models.ForeignKey(UnidadMedida, on_delete=models.PROTECT, related_name='medida_de')
    medida_a = models.ForeignKey(UnidadMedida, on_delete=models.PROTECT, related_name='medida_a')
    operacion = models.CharField(
        max_length=20,
        choices=[(operacion.value, operacion.name) for operacion in Operador]
    )
    valor = models.FloatField()
    activo = models.BooleanField(default=True)

    class Meta:
        db_table = 'conversiones_medidas'

    def __str__(self):
        return f'De {self.medida_de} a {self.medida_a}'
from django.db import models
from suscripciones.models import Suscripcion

class HistorialPago(models.Model):
    suscripcion = models.ForeignKey(Suscripcion, on_delete=models.PROTECT, null=True)
    monto = models.DecimalField(10,0)
    fecha_pago = models.DateField()
from django.db import models
from prestamos.models import CuotaPrestamo

# Prestamo
class Pago(models.Model):
    fecha_pago = models.DateField()
    cuota = models.ForeignKey(CuotaPrestamo, on_delete=models.PROTECT)
    monto_pago = models.DecimalField(max_digits=12, decimal_places=2)

    
    def __str__(self):
        return f'{self.fecha_pago}. - {self.cuota}'

    class Meta:
        db_table = 'pagos'


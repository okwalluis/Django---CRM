from django.contrib.auth.models import User

from django.db import models
from personas.models import Persona


class TipoPrestamo(models.Model):
    descripcion = models.CharField(max_length=10)
        
    class Meta:
        db_table = 'tipos_prestamo'

    def __str__(self):
        return self.descripcion

class EstadoPrestamo(models.Model):
    descripcion = models.CharField(max_length=20)

    class Meta:
        db_table = 'estados_prestamo'

    def __str__(self):
        return self.descripcion

class Prestamo(models.Model):
    nro_prestamo = models.CharField(max_length=10)
    tipo_prestamo = models.ForeignKey(TipoPrestamo, on_delete=models.PROTECT)
    fecha = models.DateField()
    persona = models.ForeignKey(Persona, on_delete=models.PROTECT)
    capital = models.DecimalField(max_digits=12, decimal_places=2)
    interes = models.FloatField()
    plazo = models.IntegerField()
    fecha_inicio  = models.DateField()
    estado_prestamo = models.ForeignKey(EstadoPrestamo, on_delete=models.PROTECT, null=True)
    
    created_by = models.ForeignKey(User, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
#    modified_by = models.ForeignKey(User, on_delete=models.PROTECT)
#    modified_at = models.DateTimeField()
    
    def __str__(self):
        return f'{self.numero}. - {self.persona.nombre} {self.persona.apellido}'

    class Meta:
        db_table = 'prestamos'
        
class CuotaPrestamo(models.Model):
    prestamo = models.ForeignKey(Prestamo, on_delete=models.PROTECT)
    nro_cuota = models.IntegerField()
    fecha_vencimiento = models.DateField()
    monto_cuota = models.DecimalField(max_digits=9, decimal_places=2)
    monto_interes = models.DecimalField(max_digits=9, decimal_places=2)
    saldo_cuota = models.DecimalField(max_digits=12, decimal_places=2)
    saldo_interes = models.DecimalField(max_digits=12, decimal_places=2)
    
    def __str__(self):
        return f'{Prestamo.__str__} {self.nro_cuota}'

    class Meta:
        db_table = 'cuotas_prestamo'
    
    
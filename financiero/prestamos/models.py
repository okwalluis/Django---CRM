from django.contrib.auth.models import User
from django.db import models
from base.personas.models import Persona
from base.empresas.models import Empresa
from base.sucursales.models import Sucursal

# Sistema de amortizacion
class SistemaPrestamo(models.Model):
    descripcion = models.CharField(max_length=50)
    activo = models.BooleanField(default=True)
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT, null=True)
    
    class Meta:
        db_table = 'sistemas_prestamo'

    def __str__(self):
        return self.descripcion

# Proposito de prestamo
class TipoPrestamo(models.Model):
    descripcion = models.CharField(max_length=50)
    activo = models.BooleanField(default=True)
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT, null=True)
    
    class Meta:
        db_table = 'tipos_prestamo'

    def __str__(self):
        return self.descripcion

# Situacion del prestamo
class EstadoPrestamo(models.Model):
    descripcion = models.CharField(max_length=20)
    activo = models.BooleanField(default=True)
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT, null=True)
    
    class Meta:
        db_table = 'estados_prestamo'

    def __str__(self):
        return self.descripcion
# Frecuencia de pagos; mensual, semestral     
class FrecuenciaPagoPrestamo(models.Model):
    descripcion = models.CharField(max_length=20)
    tasas_efectivas = models.DecimalField(max_digits=12, decimal_places=10)
    activo = models.BooleanField(default=True)
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT, null=True)
    """ Equivalencias TASA efectivas
            Anual	1
            Semestral	0,5
            Cuatrimestral	0,333333333
            Trimestral	0,25
            Bimensual	0,166666667
            Mensual	0,083333333    
    """
    
    class Meta:
        db_table = 'frecuencias_pagos'

    def __str__(self):
        return self.descripcion

# Prestamo
class Prestamo(models.Model):
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT, null=True)
    sucursal = models.ForeignKey(Sucursal, on_delete=models.PROTECT, null=True)
    nro_prestamo = models.IntegerField(editable=False)
    fecha = models.DateField()
    persona = models.ForeignKey(Persona, on_delete=models.PROTECT, null=True)
    sistema_prestamo = models.ForeignKey(SistemaPrestamo, on_delete=models.PROTECT, null=True)
    tipo_prestamo = models.ForeignKey(TipoPrestamo, on_delete=models.PROTECT, null=True)
    capital = models.DecimalField(max_digits=12, decimal_places=0)
    interes = models.FloatField() # TNA Tasa de interes anual Nominal
    frecuencia = models.ForeignKey(FrecuenciaPagoPrestamo, on_delete=models.PROTECT, null=True)
    plazo = models.IntegerField() # Nro. total de cuotas
    fecha_primer_vencimiento  = models.DateField()
    estado_prestamo = models.ForeignKey(EstadoPrestamo, on_delete=models.PROTECT, null=True)
    # interes_equivalente = models.FloatField()
    
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, related_name='created_by', editable=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    modified_by = models.ForeignKey(User, on_delete=models.PROTECT, related_name='modified_by', editable=False, null=True)
    modified_at = models.DateTimeField(editable=False, null=True)
    
    def __str__(self):
        return f'{self.nro_prestamo}. - {self.persona.nombre} {self.persona.apellido}'

    class Meta:
        db_table = 'prestamos'
        
# Cuotas del prestamo
class CuotaPrestamo(models.Model):
    prestamo = models.ForeignKey(Prestamo, on_delete=models.PROTECT)
    nro_cuota = models.IntegerField()
    fecha_vencimiento = models.DateField()
    monto_cuota = models.DecimalField(max_digits=12, decimal_places=0, default=0)
    monto_interes = models.DecimalField(max_digits=12, decimal_places=0, default=0)
    monto_capital = models.DecimalField(max_digits=12, decimal_places=0, default=0)
    # LOS SALDOS SON PARA CONTROL DE PAGOS
    saldo_cuota = models.DecimalField(max_digits=12, decimal_places=0, default=0)
    saldo_capital = models.DecimalField(max_digits=12, decimal_places=0, default=0)
    saldo_interes = models.DecimalField(max_digits=12, decimal_places=0, default=0)
    fecha_ultimo_pago = models.DateField(null=True)
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT, null=True)

    def __str__(self):
        return f'Préstamo nro. {self.prestamo.nro_prestamo}/Cuota nro. {self.nro_cuota}: {self.saldo_cuota}'

    class Meta:
        db_table = 'cuotas_prestamo'

class EstadoCuentaPrestamo(models.Model):
    persona_id = models.IntegerField()
    nro_prestamo = models.IntegerField()
    fecha = models.DateField()
    nro_cuota = models.IntegerField()
    fecha_vencimiento = models.DateField()
    monto_cuota = models.DecimalField(max_digits=10, decimal_places=0)
    saldo_cuota = models.DecimalField(max_digits=10, decimal_places=0)
    fecha_pago = models.DateField()
    cuota_actual_total = models.CharField(max_length=20)
    monto_pago = models.DecimalField(max_digits=10, decimal_places=0)
    acumulado_pago = models.DecimalField(max_digits=10, decimal_places=0)
    saldo_actual = models.DecimalField(max_digits=10, decimal_places=0)
    nro_pago = models.IntegerField()
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT, null=True)    

    class Meta:
        managed = False
        db_table = 'vw_estado_cuenta_prestamos'
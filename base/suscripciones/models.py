from django.contrib.auth.models import User

from django.db import models

class Suscripcion(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    fecha_inicio = models.DateField()
    fecha_vencimiento = models.DateField()
    estado = models.BooleanField(default=True) # Activo, expirado
    
    class Meta:
        db_table = 'suscripciones'
    
    def __str__(self):
        return f"{self.fecha_inicio} - {self.fecha_inicio}"
from django.db import models

class PlanSuscripcion(models.Model):
    descripcion = models.CharField(max_length=30, null=False)
    
    class Meta:
        db_table = 'planes_suscripciones'
    
    def __str__(self):
        return f'{self.descripcion}'
from django.db import models

class PlanSuscripcion(models.Model):
    descripcion = models.CharField(max_length=30, null=False)
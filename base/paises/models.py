from django.db import models

class Pais(models.Model):
    descripcion = models.CharField(max_length=80)
    sigla   = models.CharField(max_length=5)
    #moneda = models.ForeignKey(Moneda, on_delete=models.PROTECT)
    activo = models.BooleanField(default=True)
    
    class Meta:
        db_table = 'paises'

    def __str__(self):
        return self.descripcion
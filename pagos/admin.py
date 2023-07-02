from django.contrib import admin
from .models import Pago

class PagoAdmin(admin.ModelAdmin):
    fields = ["fecha_pago", "cuota", "monto_pago"]

admin.site.register(Pago, PagoAdmin)
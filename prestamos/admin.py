from django.contrib import admin
from .models import Prestamo, TipoPrestamo, EstadoPrestamo, CuotaPrestamo


class PrestamoAdmin(admin.ModelAdmin):
    fields = ["nro_prestamo", "tipo_prestamo", "fecha", "persona", "capital", "interes","plazo","fecha_inicio", "estado_prestamo"]

class TipoPrestamoAdmin(admin.ModelAdmin):
    fields = ["descripcion"]

class EstadoPrestamoAdmin(admin.ModelAdmin):
    fields = ["descripcion"]
    
class CuotaPrestamoAdmin(admin.ModelAdmin):
    fields = ["prestamo", "nro_cuota", "fecha_vencimiento", "monto_cuota", "monto_interes", "saldo_cuota", "saldo_interes"]


#admin.site.register(Question)
#admin.site.register(Choice)
admin.site.register(Prestamo, PrestamoAdmin)
admin.site.register(TipoPrestamo, TipoPrestamoAdmin)
admin.site.register(EstadoPrestamo, EstadoPrestamoAdmin)
admin.site.register(CuotaPrestamo, CuotaPrestamoAdmin)
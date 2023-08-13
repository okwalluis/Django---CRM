from django.contrib import admin
from .models import Prestamo, TipoPrestamo, EstadoPrestamo, CuotaPrestamo, SistemaPrestamo, FrecuenciaPagoPrestamo


class PrestamoAdmin(admin.ModelAdmin):
    fields = ["nro_prestamo", "tipo_prestamo", "fecha", 
              "persona", "capital", "interes",
              "plazo","fecha_primer_vencimiento", "estado_prestamo"]

class SistemaPrestamoAdmin(admin.ModelAdmin):
    fields = ["descripcion", "activo"]

class TipoPrestamoAdmin(admin.ModelAdmin):
    fields = ["descripcion", "activo"]

class EstadoPrestamoAdmin(admin.ModelAdmin):
    fields = ["descripcion", "activo"]
    
class FrecuenciaPagoPrestamoAdmin(admin.ModelAdmin):
    fields = ["descripcion", "tasas_efectivas","activo"]

class CuotaPrestamoAdmin(admin.ModelAdmin):
    fields = ["prestamo", "nro_cuota", "fecha_vencimiento", "monto_cuota", "monto_interes", "monto_capital", "saldo_cuota", "saldo_interes", "saldo_capital"]


#admin.site.register(Question)
#admin.site.register(Choice)

admin.site.register(Prestamo, PrestamoAdmin)
admin.site.register(SistemaPrestamo, SistemaPrestamoAdmin)
admin.site.register(TipoPrestamo, TipoPrestamoAdmin)
admin.site.register(EstadoPrestamo, EstadoPrestamoAdmin)
admin.site.register(FrecuenciaPagoPrestamo, FrecuenciaPagoPrestamoAdmin)
admin.site.register(CuotaPrestamo, CuotaPrestamoAdmin)
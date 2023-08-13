from django.contrib import admin


class LoteAdmin(admin.ModelAdmin):
    fields = ["empresa","producto","nro_lote","fecha_elaboracion", "fecha_vencimiento", "descripcion", "activo"]
    
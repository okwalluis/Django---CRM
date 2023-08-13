from django.contrib import admin


class DepositoAdmin(admin.ModelAdmin):
    fields = ["empresa", "sucursal", "descripcion", "es_virtual", "activo"]
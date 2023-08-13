from django.contrib import admin

class UnidadMedidaAdmin(admin.ModelAdmin):
    fields = ["descripcion", "sigla", "activo"]
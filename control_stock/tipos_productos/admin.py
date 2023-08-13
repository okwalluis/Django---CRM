from django.contrib import admin

class TipoProductoAdmin(admin.ModelAdmin):
    fields = ["descripcion", "activo"]
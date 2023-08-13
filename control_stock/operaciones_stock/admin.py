from django.contrib import admin

class OperacionStockAdmin(admin.ModelAdmin):
    fields = ["empresa", "descripcion", "operacion", "activo"]
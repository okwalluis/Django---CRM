from django.contrib import admin

class ClaseProductoAdmin(admin.ModelAdmin):
    fields = ["empresa", "descripcion", "activo"]
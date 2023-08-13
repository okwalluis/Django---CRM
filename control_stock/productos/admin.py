from django.contrib import admin

class ProductoAdmin(admin.ModelAdmin):
    fields = ["empresa", "descripcion", "familia", "grupo", "impuesto","clase","tipo",""]
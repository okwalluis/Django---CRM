from django.contrib import admin

class ConversionMedidaAdmin(admin.ModelAdmin):
    fields = ["medida_de", "medida_a", "operacion", "valor"]
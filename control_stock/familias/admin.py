from django.contrib import admin

class FamiliaAdmin(admin.ModelAdmin):
    fields = ["empresa","descripcion","activo"]
from django.contrib import admin

class GrupoAdmin(admin.ModelAdmin):
    fields = ["empresa","familia","descripcion","activo"]
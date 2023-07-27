from django.contrib import admin
from pagares.models import Pagare

class PagareAdmin(admin.ModelAdmin):
    fields = ["id", "fecha_emision", "cuota", "monto_pagare"]

admin.site.register(Pagare, PagareAdmin)

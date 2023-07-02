from django.contrib import admin
from .models import Persona, TipoPersona, Sexo, Direccion, Telefono

class PersonaAdmin(admin.ModelAdmin):
    fields = ["nombre", "apellido", 
              "razon_social", "tipo_persona",
              "sexo", "fecha_nacimiento", 
              "es_cliente", "es_proveedor"]

class TipoPersonaAdmin(admin.ModelAdmin):
    fields = ["descripcion"]

class SexoAdmin(admin.ModelAdmin):
    fields = ["descripcion"]

class DireccionAdmin(admin.ModelAdmin):
    fields = ["descripcion"]

class TelefonoAdmin(admin.ModelAdmin):
    fields = ["persona","numero"]

#admin.site.register(Question)
#admin.site.register(Choice)
admin.site.register(Persona, PersonaAdmin)
admin.site.register(TipoPersona, TipoPersonaAdmin)
admin.site.register(Sexo, SexoAdmin)
admin.site.register(Direccion, DireccionAdmin)
admin.site.register(Telefono, TelefonoAdmin)


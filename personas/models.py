from django.db import models

class TipoPersona(models.Model):
    descripcion = models.CharField(max_length=50)
    activo = models.BooleanField(default=True)

    class Meta:
        db_table = 'tipos_persona'

    def __str__(self):
        return self.descripcion

class Sexo(models.Model):
    descripcion = models.CharField(max_length=10)
    
    class Meta:
        db_table = 'sexos'

    def __str__(self):
        return self.descripcion

class Persona(models.Model):
    nombre = models.CharField(max_length=200) 
    apellido = models.CharField(max_length=100)
    tipo_persona = models.ForeignKey(TipoPersona, on_delete=models.PROTECT, null=True)
    razon_social = models.CharField(max_length=200)
    fecha_nacimiento = models.DateField(null=True)
    sexo = models.ForeignKey(Sexo, on_delete=models.PROTECT, null=True)
    es_cliente = models.BooleanField(default=False)
    es_proveedor = models.BooleanField(default=False)
    activo = models.BooleanField(default=True)

    class Meta:
        db_table = 'personas'

    def __str__(self) -> str:
        return f'{self.nombre} {self.apellido}'

class Direccion(models.Model):
    persona = models.ForeignKey(Persona, on_delete=models.PROTECT)
    descripcion = models.CharField(max_length=100)
    por_defecto = models.BooleanField(default=False)

    class Meta:
        db_table = 'direcciones'

    def __str__(self):
        return f'{self.descripcion}'

class Telefono(models.Model):
    persona = models.ForeignKey(Persona, on_delete=models.PROTECT)
    numero = models.CharField(max_length=100)
    por_defecto = models.BooleanField(default=False)

    class Meta:
        db_table = 'telefonos'

    def __str__(self):
        return f'{self.numero}'

class TipoDocumento(models.Model):
    descripcion = models.CharField(max_length=100)
    activo = models.BooleanField(default=True)

    class Meta:
        db_table = 'tipos_documento'

    def __str__(self):
        return f'{self.descripcion}'
    
class Documento(models.Model):
    tipo_documento = models.ForeignKey(TipoDocumento, on_delete=models.PROTECT)
    persona = models.ForeignKey(Persona, on_delete=models.PROTECT)
    numero = models.CharField(unique=True, null=False, max_length=30)

    class Meta:
        db_table = 'documentos'

    def __str__(self):
        return f'{self.numero}'
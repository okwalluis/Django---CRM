from django import forms
from .models import TipoPersona, Persona, Sexo, Direccion, Telefono

class TipoPersonaForm(forms.ModelForm):
    class Meta:
        model = TipoPersona
        fields = ['descripcion']

class SexoForm(forms.ModelForm):
    class Meta:
        model = Sexo
        fields = ['descripcion']

class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = ['nombre', 'apellido', 'razon_social', 'tipo_persona', 'sexo', 'fecha_nacimiento','es_cliente', 'es_proveedor']
        widgets = {
            'nombre': forms.TextInput(attrs={'type':'text','class': 'form-control', 'placeholder': 'Ingrese el nombre', 'name':'nombre'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el apellido'}),
            'razon_social': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese la razón social'}),
            'tipo_persona': forms.Select(attrs={'class': 'form-control'}),
            'sexo': forms.Select(attrs={'class': 'form-control'}),
            'fecha_nacimiento' : forms.TextInput(attrs={'type':'date', 'class': 'form-control', 'placeholder': 'Fecha de nacimiento'}),
            'es_cliente': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'es_proveedor': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
         
class DireccionForm(forms.ModelForm):
    class Meta:
        model = Direccion
        fields = ['persona', 'descripcion', 'por_defecto']

class TelefonoForm(forms.ModelForm):
    class Meta:
        model = Telefono
        fields = ['persona', 'numero', 'por_defecto']
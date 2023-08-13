from django import forms
from .models import TipoPersona, Persona, Sexo, Direccion, Telefono, Documento, TipoDocumento

class TipoPersonaForm(forms.ModelForm):
    class Meta:
        model = TipoPersona
        fields = ['descripcion']

class SexoForm(forms.ModelForm):
    class Meta:
        model = Sexo
        fields = ['descripcion']

class PersonaForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PersonaForm, self).__init__(*args, **kwargs)
        self.fields['razon_social'].required = False

    def clean(self):
        cleaned_data = super(PersonaForm, self).clean()
        tipo_persona = cleaned_data.get('tipo_persona')

        if tipo_persona == 1:
            razon_social = cleaned_data.get('razon_social')
            if not razon_social:
                self.add_error('razon_social', 'La razón social es requerida para personas de tipo 1.')
                
    class Meta:
        model = Persona
        fields = ['nombre', 'apellido', 'tipo_persona', 'razon_social', 'sexo', 'fecha_nacimiento','es_cliente', 'es_proveedor']
        widgets = {
            'nombre': forms.TextInput(attrs={'type':'text','class': 'form-control', 'placeholder': 'Ingrese el nombre', 'name':'nombre'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el apellido'}),
            'tipo_persona': forms.Select(attrs={'id':'id_tipo_persona','name':'id_tipo_persona','class': 'form-control'}),
            'razon_social': forms.TextInput(attrs={'id': 'id_razon_social', 'name': 'id_razon_social','class': 'form-control', 'placeholder': 'Ingrese la razón social'}),
            'sexo': forms.Select(attrs={'id': 'id_sexo', 'name': 'id_sexo', 'class': 'form-control'}),
            'fecha_nacimiento' : forms.TextInput(attrs={'type':'date', 'class': 'form-control', 'placeholder': 'Fecha de nacimiento'}),
            'es_cliente': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'es_proveedor': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
         
class DireccionForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        persona = kwargs.pop('persona', None)
        super().__init__(*args, **kwargs)
        if persona:
            self.fields['persona'].queryset = Persona.objects.filter(id=persona.id)

    class Meta:
        model = Direccion
        fields = ['persona', 'descripcion', 'por_defecto']
        labels = {
            'persona': 'Persona',
            'descripcion': 'Descripción',
            'por_defecto': 'Por Defecto',
        }
        widgets = {
            'persona': forms.Select(attrs={'class': 'form-control'}),
            'descripcion': forms.TextInput(attrs={'type': 'text', 'class': 'form-control'}),
            'por_defecto': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

class TelefonoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        persona = kwargs.pop('persona', None)
        super().__init__(*args, **kwargs)
        if persona:
            self.fields['persona'].queryset = Persona.objects.filter(id=persona.id)
    
    class Meta:
        model = Telefono
        fields = ['persona', 'numero', 'por_defecto']
        labels = {
            'numero': 'Número',
        }
class TipoDocumentoForm(forms.ModelForm):
    class Meta:
        model = TipoDocumento
        fields = ['descripcion']
class DocumentoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        persona = kwargs.pop('persona', None)
        super().__init__(*args, **kwargs)
        if persona:
            self.fields['persona'].queryset = Persona.objects.filter(id=persona.id)
    
    class Meta:
        model = Documento
        fields = ['persona', 'tipo_documento', 'numero']
        labels = {
            'numero': 'Número',
        }
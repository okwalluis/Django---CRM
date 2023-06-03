from django import forms
from .models import TipoPersona, Persona, Sexo, Direccion, Telefono

class TipoPersonaForm(forms.ModelForm):
    class Meta:
        model = TipoPersona
        fields = '__all__'

class SexoForm(forms.ModelForm):
    class Meta:
        model = Sexo
        fields = '__all__'

class PersonaForm(forms.ModelForm):
    nombre = forms.CharField(label='Nombre', max_length=200)
    apellido = forms.CharField(label='Apellido', max_length=100)
    razon_social = forms.CharField(label='Razón Social', max_length=200)

    #class Meta:
    #    model = Persona
    #    fields = '__all__'
    #fields = ['question_text'] # usamos los nombres definidos en el modelo
    #fields = '__all__' # aqui decimos que queremos muestre todos los fields.        

class DireccionForm(forms.ModelForm):
    class Meta:
        model = Direccion
        fields = '__all__'

class TelefonoForm(forms.ModelForm):
    class Meta:
        model = Telefono
        fields = '__all__'
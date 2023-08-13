from django import forms
from base.paises.models import Pais

class PaisForm(forms.ModelForm):
    class Meta:
        model = Pais
        fields = '__all__'


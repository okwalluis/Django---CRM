from django import forms
from control_stock.grupos.models import GrupoProducto

class GrupoProductoForm(forms.ModelForm):
    class Meta:
        model = GrupoProducto
        fields = '__all__'
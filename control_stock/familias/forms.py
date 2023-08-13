from django import forms
from control_stock.familias.models import FamiliaProducto

class FamiliaProductoForm(forms.ModelForm):
    class Meta:
        model = FamiliaProducto
        fields = '__all__'
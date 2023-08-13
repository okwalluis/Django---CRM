from django import forms
from control_stock.tipos_productos.models import TipoProducto

class TipoProductoForm(forms.ModelForm):
    class Meta:
        model = TipoProducto
        fields = '__all__'
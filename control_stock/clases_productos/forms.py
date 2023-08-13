from django import forms
from control_stock.clases_productos.models import ClaseProducto

class ClaseProductoForm(forms.ModelForm):
    class Meta:
        model = ClaseProducto
        fields = '__all__'


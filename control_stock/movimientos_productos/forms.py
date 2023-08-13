from django import forms
from control_stock.movimientos_productos.models import MovimientoProducto, MovimientoProductoLote

class MovimientoProductoForm(forms.ModelForm):
    class Meta:
        model = MovimientoProducto
        fields = '__all__'


class MovimientoProductoLoteForm(forms.ModelForm):
    class Meta:
        model = MovimientoProductoLote 
        fields = '__all__'
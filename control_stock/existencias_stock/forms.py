from django import forms
from control_stock.existencias_stock.models import ExistenciaProducto, ExistenciaProductoLote

class ExistenciaProductoForm(forms.ModelForm):
    class Meta:
        model = ExistenciaProducto
        fields = '__all__'


class ExistenciaProductoLoteForm(forms.ModelForm):
    class Meta:
        model = ExistenciaProductoLote
        fields = '__all__'
from django import forms
from control_stock.unidades_medidas.models import UnidadMedida

class UnidadMedidaForm(forms.ModelForm):
    class Meta:
        model = UnidadMedida
        fields = '__all__'
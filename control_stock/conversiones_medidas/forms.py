from django import forms
from control_stock.conversiones_medidas.models import ConversionMedida

class ConversionMedidaForm(forms.ModelForm):
    class Meta:
        model = ConversionMedida
        fields = '__all__'
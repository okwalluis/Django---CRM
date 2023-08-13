from django import forms
from control_stock.depositos.models import Deposito

class DepositoForm(forms.ModelForm):
    class Meta:
        model = Deposito
        fields = '__all__'
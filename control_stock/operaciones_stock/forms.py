from django import forms
from control_stock.operaciones_stock.models import OperacionStock

class OperacionStockForm(forms.ModelForm):
    class Meta:
        model = OperacionStock
        fields = '__all__'
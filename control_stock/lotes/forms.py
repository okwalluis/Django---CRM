from django import forms
from control_stock.lotes.models import Lote

class LoteForm(forms.ModelForm):
    class Meta:
        model = Lote
        fields = '__all__'
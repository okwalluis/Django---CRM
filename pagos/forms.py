from django import forms
from datetime import date
from .models import Pago
from prestamos.models import CuotaPrestamo


class PagoForm(forms.ModelForm):
    fecha_pago = forms.DateField(
        initial=date.today(),
        widget=forms.TextInput(
            attrs={'type': 'date', 'class': 'form-control', 'placeholder': 'Fecha de pago'})
    )
    cuota = forms.ModelChoiceField(
        queryset=CuotaPrestamo.objects.all(),
        widget=forms.Select(
            attrs={'class': 'form-control', 'placeholder': 'Cuota'})
    )
    monto_pago = forms.DecimalField(
        initial=0,
        widget=forms.TextInput(
            attrs={'type': 'number', 'class': 'form-control', 'placeholder': '0', 'min': 0})
    )

    class Meta:
        model = Pago
        fields = ['fecha_pago', 'cuota', 'monto_pago']
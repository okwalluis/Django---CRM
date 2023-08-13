from django import forms
from base.historial_pagos.models import HistorialPago

class HistorialPagoForm(forms.ModelForm):
    class Meta:
        model = HistorialPago
        fields = '__all__'


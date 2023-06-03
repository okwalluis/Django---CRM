from django import forms
from .models import TipoPrestamo, EstadoPrestamo, Prestamo, CuotaPrestamo

class TipoPrestamoForm(forms.ModelForm):
    class Meta:
        model = TipoPrestamo
        fields = '__all__'

class EstadoPrestamoForm(forms.ModelForm):
    class Meta:
        model = EstadoPrestamo
        fields = '__all__'

class PrestamoForm(forms.ModelForm):
    class Meta:
        model = Prestamo
        fields = '__all__'

class CuotaPrestamoForm(forms.ModelForm):
    class Meta:
        model = CuotaPrestamo
        fields = '__all__'
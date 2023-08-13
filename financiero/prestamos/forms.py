from django import forms
from decimal import Decimal
from datetime import date
from .models import TipoPrestamo, EstadoPrestamo, Prestamo, CuotaPrestamo, SistemaPrestamo, FrecuenciaPagoPrestamo
from base.personas.models import Persona


class SistemaPrestamoForm(forms.ModelForm):
    class Meta:
        model = SistemaPrestamo
        fields = '__all__'

class TipoPrestamoForm(forms.ModelForm):
    class Meta:
        model = TipoPrestamo
        fields = '__all__'

class EstadoPrestamoForm(forms.ModelForm):
    class Meta:
        model = EstadoPrestamo
        fields = '__all__'

class FrecuenciaPagoPrestamoForm(forms.ModelForm):
    class Meta:
        model = FrecuenciaPagoPrestamo
        fields = '__all__'

class PrestamoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)  # Get the user from the kwargs
        self.operacion = kwargs.pop('operacion', None)
        super().__init__(*args, **kwargs)

        #fecha_vencimiento_desde = forms.DateField(widget=forms.TextInput(attrs={'type':'date', 'class': 'form-control'}), required=False)
        if self.operacion == 'E':
            self.fields['sistema_prestamo'].queryset = SistemaPrestamo.objects.filter(activo = True)
            self.fields['tipo_prestamo'].queryset = TipoPrestamo.objects.filter(activo = True)
            self.fields['frecuencia'].queryset = FrecuenciaPagoPrestamo.objects.filter(activo = True)
            self.fields['estado_prestamo'].queryset = EstadoPrestamo.objects.filter(activo = True)
        else:
            self.fields['persona'].queryset = Persona.objects.filter(es_cliente=True)           
            self.fields['sistema_prestamo'].queryset = SistemaPrestamo.objects.all()
            self.fields['tipo_prestamo'].queryset = TipoPrestamo.objects.all()
            self.fields['frecuencia'].queryset = FrecuenciaPagoPrestamo.objects.all()
            self.fields['estado_prestamo'].queryset = EstadoPrestamo.objects.filter(id=1)
            
            self.fields['fecha'].initial = date.today()
            self.fields['sistema_prestamo'].initial = 1 # Frances
            self.fields['tipo_prestamo'].initial = 1 # Persona
            self.fields['frecuencia'].initial = 7 # Mensual
            self.fields['estado_prestamo'].initial = 1 # Activo
            
    class Meta:
        model = Prestamo
        fields = ['fecha', 
                  'persona', 
                  'sistema_prestamo', 
                  'tipo_prestamo', 
                  'capital', 
                  'interes',
                  'frecuencia',
                  'plazo',
                  'fecha_primer_vencimiento',
                  'estado_prestamo']
        widgets = {
            'fecha': forms.DateInput(attrs={'type':'date', 'class': 'form-control', 'placeholder': 'Fecha de emisión'}),
            'persona': forms.Select(attrs={'type':'select', 'class': 'form-control', 'placeholder': 'Cliente', 'name':'persona'}),
            'sistema_prestamo': forms.Select(attrs={'type':'select', 'class': 'form-control', 'placeholder': 'Sistema de Préstamo'}),
            'tipo_prestamo': forms.Select(attrs={'type':'select', 'class': 'form-control', 'placeholder': 'Tipo de préstamo'}),
            'capital': forms.TextInput(attrs={'type':'number','class': 'form-control','placeholder': '0', 'min':0}),
            'interes': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '0,00', 'step': Decimal('0.01'), 'min': Decimal('0.00')}),
            'frecuencia': forms.Select(attrs={'type':'select', 'class': 'form-control', 'placeholder': 'Frecuencia de pago'}),
            'plazo':forms.TextInput(attrs={'type':'number', 'class': 'form-control', 'placeholder': 'Plazo o número de cuotas', 'min':0}),
            'fecha_primer_vencimiento':forms.TextInput(attrs={'type':'date', 'class': 'form-control', 'placeholder': 'Fecha primer vencimiento', 'label':'Fecha primer Vto.:'}),
            'estado_prestamo': forms.Select(attrs={'type':'select', 'class': 'form-control'}),
        }

class CuotaPrestamoForm(forms.ModelForm):
    class Meta:
        model = CuotaPrestamo
        fields = '__all__'

class EstadoCuentaPrestamoForm(forms.Form):
    persona = forms.ModelChoiceField(queryset=Persona.objects.filter(es_cliente=True))
    prestamo = forms.ModelChoiceField(queryset=Prestamo.objects.all(), required=False)
    fecha_emision_desde = forms.DateField(widget=forms.TextInput(attrs={'type':'date', 'class': 'form-control'}), required=False)
    fecha_emision_hasta = forms.DateField(widget=forms.TextInput(attrs={'type':'date', 'class': 'form-control'}), required=False)
    fecha_vencimiento_desde = forms.DateField(widget=forms.TextInput(attrs={'type':'date', 'class': 'form-control'}), required=False)
    fecha_vencimiento_hasta = forms.DateField(widget=forms.TextInput(attrs={'type':'date', 'class': 'form-control'}), required=False)
    
    class Meta:
        model = Prestamo
        fields = ['persona', 
                  'prestamo',
                  'fecha_emision_desde',
                  'fecha_emision_hasta',
                  'fecha_vencimiento_desde',
                  'fecha_vencimiento_hasta']
        widgets = {
            'persona': forms.Select(attrs={'type':'select', 'class': 'form-control', 'placeholder': 'Cliente'}),
            'prestamo': forms.Select(attrs={'type':'select', 'class': 'form-control'}),
            'fecha_emision_desde': forms.TextInput(attrs={'type':'date', 'class': 'form-control'}),
            'fecha_emision_hasta': forms.TextInput(attrs={'type':'date', 'class': 'form-control'}),
            'fecha_vencimiento_desde': forms.TextInput(attrs={'type':'date', 'class': 'form-control'}),
            'fecha_vencimiento_hasta': forms.TextInput(attrs={'type':'date', 'class': 'form-control'}),            
        }
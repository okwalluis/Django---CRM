from django import forms
from decimal import Decimal
from datetime import date
from .models import TipoPrestamo, EstadoPrestamo, Prestamo, CuotaPrestamo, SistemaPrestamo, FrecuenciaPagoPrestamo
from personas.models import Persona


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
        super().__init__(*args, **kwargs)
        self.fields['persona'].queryset = Persona.objects.filter(es_cliente=True)
        self.fields['sistema_prestamo'].queryset = SistemaPrestamo.objects.all()
        self.fields['tipo_prestamo'].queryset = TipoPrestamo.objects.all()
        self.fields['frecuencia'].queryset = FrecuenciaPagoPrestamo.objects.all()
        #self.fields['estado_prestamo'].queryset = EstadoPrestamo.objects.filter(id=1)
        
        self.fields['fecha'].initial = date.today()
        self.fields['sistema_prestamo'].initial = 1 # Frances
        self.fields['tipo_prestamo'].initial = 1 # Persona
        self.fields['frecuencia'].initial = 7 # Mensual
        #self.fields['estado_prestamo'].initial = 1 # Activo
        

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
                  'fecha_primer_vencimiento']
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
        }
        #initial = {
        #    'estado_prestamo': 1,  # Valor inicial para el campo 'estado_prestamo'
        #}

class PrestamoEditarForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)  # Get the user from the kwargs
        super().__init__(*args, **kwargs)
        #self.fields['persona'].queryset = Persona.objects.filter(es_cliente=True)
        self.fields['sistema_prestamo'].queryset = SistemaPrestamo.objects.filter(activo = True)
        self.fields['tipo_prestamo'].queryset = TipoPrestamo.objects.filter(activo = True)
        self.fields['frecuencia'].queryset = FrecuenciaPagoPrestamo.objects.filter(activo = True)
        self.fields['estado_prestamo'].queryset = EstadoPrestamo.objects.filter(activo = True)

    class Meta:
        model = Prestamo
        fields = [#'nro_prestamo',
                  'fecha', 
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
            #'nro_prestamo': forms.TextInput(attrs={'class': 'form-control', 'disabled':True}),
            'fecha': forms.TextInput(attrs={'type':'date', 'class': 'form-control', 'disabled':True}),
            'persona': forms.Select(attrs={'type':'select', 'class': 'form-control', 'placeholder': 'Cliente', 'name':'persona', 'disabled':True}),
            'sistema_prestamo': forms.Select(attrs={'type':'select', 'class': 'form-control'}),
            'tipo_prestamo': forms.Select(attrs={'type':'select', 'class': 'form-control'}),
            'capital': forms.TextInput(attrs={'type':'number','class': 'form-control','placeholder': '0', 'min':0}),
            'interes': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '0,00', 'step': Decimal('0.01'), 'min': Decimal('0.00')}),
            'frecuencia': forms.Select(attrs={'type':'select', 'class': 'form-control'}),
            'plazo':forms.TextInput(attrs={'type':'number', 'class': 'form-control', 'min':0}),
            'fecha_primer_vencimiento':forms.TextInput(attrs={'label':'Fecha primer Vto.:','type':'date', 'class': 'form-control'}),
            'estado_prestamo': forms.Select(attrs={'type':'select', 'class': 'form-control'}),
        }

class CuotaPrestamoForm(forms.ModelForm):
    class Meta:
        model = CuotaPrestamo
        fields = '__all__'
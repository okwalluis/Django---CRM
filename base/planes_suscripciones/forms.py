from django import forms
from base.planes_suscripciones.models import PlanSuscripcion

class PlanSuscripcionForm(forms.ModelForm):
    class Meta:
        model = PlanSuscripcion
        fields = '__all__'


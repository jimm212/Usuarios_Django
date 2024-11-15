from django import forms
from .models import Oferta

class OfertaForm(forms.ModelForm):
    fecha_inicio = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}), input_formats=['%d-%m-%YT%H:%M'])
    fecha_fin    = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}), input_formats=['%d-%m-%YT%H:%M'])
    class Meta:
        model = Oferta
        fields = ['producto', 'porcentaje_descuento', 'fecha_inicio', 'fecha_fin']

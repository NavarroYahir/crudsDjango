from django import forms
from .models import Cosa

class CosaForm(forms.ModelForm):
    class Meta:
        model = Cosa
        fields = ['nombre', 'descripcion', 'involucrados']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control'}),
            'involucrados': forms.NumberInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'nombre': 'Nombre',
            'descripcion': 'Descripción',
            'involucrados': 'Número de involucrados',
        }
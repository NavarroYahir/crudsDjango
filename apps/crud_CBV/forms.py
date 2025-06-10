from django import forms
from apps.crud_ninja.models import Cosa

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

    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if not nombre:
            raise forms.ValidationError("El nombre es obligatorio.")
        if len(nombre) < 3:
            raise forms.ValidationError("El nombre debe tener al menos 3 caracteres.")
        return nombre

    def clean_involucrados(self):
        involucrados = self.cleaned_data.get('involucrados')
        if involucrados is None:
            raise forms.ValidationError("Debes ingresar un número de involucrados.")
        if involucrados < 1:
            raise forms.ValidationError("Debe haber al menos un involucrado.")
        return involucrados

    def clean_descripcion(self):
        descripcion = self.cleaned_data.get('descripcion')
        if not descripcion or descripcion.strip() == "":
            raise forms.ValidationError("La descripción no puede estar vacía.")
        return descripcion

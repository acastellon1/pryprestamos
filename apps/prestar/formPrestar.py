from django import forms
from apps.prestar.models import Prestar


class PrestarForm(forms.ModelForm):

    class Meta:
        model = Prestar

        fields = [
            'fechaDev',
            'fechaPres',
            'usuario',
            'ejemplar',
            
        ]

        labels = {
            'fechaDev': 'Ingrese la fecha de devolución',
            'fechaPres': 'Ingrese la fecha de prestamo',
            'usuario': 'Seleccione el usuario',
            'ejemplar': 'Seleccione el ejemplar',
            
        }

        widgets = {
            'fechaDev': forms.TextInput(attrs={'class': 'form-control'}),
            'fechaPres': forms.TextInput(attrs={'class': 'form-control'}),
            'usuario': forms.Select(attrs={'class': 'form-control'}),
            'ejemplar': forms.Select(attrs={'class': 'form-control'}),
            
        }
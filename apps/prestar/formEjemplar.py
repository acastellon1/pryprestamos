from django import forms
from apps.prestar.models import Ejemplar


class EjemplarForm(forms.ModelForm):

    class Meta:
        model = Ejemplar

        fields = [
            'localizacion',
            'libro'
        ]

        labels = {
            'localizacion': 'Ingrese la localización',
            'libro': 'Seleccione el libro',
            
        }

        widgets = {
            'localizacion': forms.TextInput(attrs={'class': 'form-control'}),
            'libro': forms.Select(attrs={'class': 'form-control'}),
        }
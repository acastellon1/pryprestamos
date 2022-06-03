from django import forms
from apps.prestar.models import Usuario


class UsuarioForm(forms.ModelForm):

    class Meta:
        model = Usuario

        fields = [
            'nombre',
            'apellidos',
            'direccion',
            'telefono',
            
        ]

        labels = {
            'nombre': 'Ingrese el nombre',
            'apellidos': 'Ingrese los apellidos',
            'direccion': 'Ingrese la direccion',
            'telefono': 'Ingrese el telefono',
            
        }

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellidos': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            
        }
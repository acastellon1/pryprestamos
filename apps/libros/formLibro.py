from django import forms
from apps.libros.models import Libro


class LibroForm(forms.ModelForm):

    class Meta:
        model = Libro

        fields = [
            'titulo',
            'noPagina',
            'editorial',
            'isbn',
            'autor',
            
        ]

        labels = {
            'titulo': 'Ingrese el titulo',
            'noPagina': 'Ingrese el numero de paginas',
            'editorial': 'Ingrese la editorial',
            'isbn': 'Ingrese el ISBN',
            'autor': 'Seleccione el autor',
            
        }

        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'noPagina': forms.TextInput(attrs={'class': 'form-control'}),
            'editorial': forms.TextInput(attrs={'class': 'form-control'}),
            'isbn': forms.TextInput(attrs={'class': 'form-control'}),
            'autor': forms.Select(attrs={'class': 'form-control'}),
            
        }
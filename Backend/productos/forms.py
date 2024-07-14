from django import forms
from .models import *


class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = [
            'nombres', 
            'apellido_paterno', 
            'apellido_materno', 
            'rut', 
            'telefono', 
            'correo', 
            'curriculum', 
            'jornada', 
            'comentarios'
        ]
        widgets = {
            'nombres': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido_paterno': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido_materno': forms.TextInput(attrs={'class': 'form-control'}),
            'rut': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'correo': forms.EmailInput(attrs={'class': 'form-control'}),
            'curriculum': forms.FileInput(attrs={'class': 'form-control'}),
            'jornada': forms.Select(attrs={'class': 'form-control'}),
            'comentarios': forms.Textarea(attrs={'class': 'form-control'}),
        }
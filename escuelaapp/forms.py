from dataclasses import fields
from django import forms
from .models import *

class ProfesorForm(forms.ModelForm):
    username = forms.CharField(max_length=20, label="Usuario", widget=forms.TextInput(
        attrs={
            'class': "form-control",
            'placeholder': "Nombre de usuario"
        }
    ))
    password = forms.CharField(max_length=40, widget=(forms.PasswordInput(
        attrs={
            'class': "form-control"
        }
    )))
    email = forms.EmailField()
    nombres = forms.CharField(max_length=120)
    apellidos = forms.CharField(max_length=120)
    
    class Meta:
        model = Profesor
        fields = ['cod_profesor', 'direccion', 'telefono']
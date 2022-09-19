from dataclasses import fields
from django.contrib.auth.models import Group
from django.contrib.contenttypes.models import ContentType
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
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={
            'class': "form-control"
        }
    ))
    nombres = forms.CharField(max_length=120, widget=(forms.TextInput(
        attrs={
            'class': "form-control"
        }
    )))
    apellidos = forms.CharField(max_length=120, widget=(forms.TextInput(
        attrs={
            'class': "form-control"
        }
    )))
    rol = forms.ModelChoiceField(label="Rol", queryset=Group.objects.all(), widget=forms.Select(
        attrs={
            'class': 'form-select'
        }
    ))
    cod_profesor = forms.CharField(max_length=12, widget=(forms.TextInput(
        attrs={
            'class': "form-control"
        }
    )))
    telefono = forms.CharField(max_length=10, widget=(forms.TextInput(
        attrs={
            'class': "form-control"
        }
    )))
    direccion = forms.CharField(max_length=120, widget=(forms.TextInput(
        attrs={
            'class': "form-control"
        }
    )))
    
    class Meta:
        model = Profesor
        fields = ['cod_profesor', 'direccion', 'telefono']
        
class GroupsForm(forms.ModelForm):
    name = forms.CharField(max_length=80, label='Rol', widget=forms.TextInput(
        attrs={
            'class': 'form-control'
        }
    ))
    contenido = forms.ModelChoiceField(queryset=ContentType.objects.filter(app_label='escuelaapp'), widget=forms.Select(
        attrs={
            'class': 'form-select'
        }
    ))
    
    class Meta:
        model = Group
        fields = '__all__'
        
class LoginForm(forms.Form):
    username = forms.CharField(max_length=80, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Usuario'
        }
    ))
    password = forms.CharField(max_length=80, widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'password'
        }
    ))
    
class ProgramaForm(forms.ModelForm):
    nombre = forms.CharField(max_length=185)
    descripcion = forms.CharField(widget=forms.Textarea())
    
    class Meta:
        model = Programa
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super().__init__()
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            visible.field.widget.attrs['placeholder'] = f'{visible.field.label} del programa'
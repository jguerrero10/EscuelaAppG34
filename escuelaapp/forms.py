from dataclasses import fields
from django import forms
from .models import *

class ProfesorForm(forms.ModelForm):
    class Meta:
        model = Profesor
        fields = '__all__'
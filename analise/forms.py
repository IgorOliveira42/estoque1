from django import forms
from .models import Analises

class FormAnalises(forms.ModelForm):
    class Meta: 
        model = Analises
        fields = [
            'analise_produto',
            'analise_quantidade',
            'conformidade',
            'status',
            ]
        
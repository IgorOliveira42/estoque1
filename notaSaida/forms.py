from django import forms
from .models import NotaSaida

class FormNotaSaida(forms.ModelForm):
    class Meta: 
        model = NotaSaida
        fields = [
            'saida_produto',
            'saida_quant',
            'saida_valor',
            'saida_data',
            'saida_cidade',
        ]
        
from django import forms
from .models import Cervejas

class FormProdutos(forms.ModelForm):
    class Meta:
        model = Cervejas
        fields = ['rotulo','embalagem','lote','quantidade','conformidade']
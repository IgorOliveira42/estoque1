from django.db import models
from cerveja.models import Cervejas
from cidade.models import Cidades

class NotaSaida(models.Model):
    saida_produto=models.ForeignKey(Cervejas, on_delete=models.PROTECT)
    saida_quant=models.IntegerField('Quantidade', default=0)
    saida_valor=models.DecimalField('Valor',decimal_places=2, max_digits=8)
    saida_data=models.DateField('Data de Saída', auto_now=False)
    saida_cidade= models.ForeignKey(Cidades, on_delete=models.PROTECT)

    def __str__(self):
        return self.saida_produto.rotulo+'Vencimento'+self.saida_produto.vencimento
    
    class Meta:
        verbose_name='Nota de Saida'
        verbose_name_plural='Notas de Saida'
        ordering=['id']
# Create your models here.

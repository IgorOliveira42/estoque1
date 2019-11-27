from django.db import models
from datetime import datetime,timedelta, date
from cerveja.models import Cervejas

conform_select=(('Não Conforme - Em testes','Não Conforme - Em testes'),('Conforme - Testado','Conforme - Testado'),('Não Conforme - Testado','Não Conforme - Testado'),)
status_select=(('Em Análise','Em Análise'),('Passou','Passou'),('Descarte','Descarte'),)

class Analises(models.Model):
    analise_produto = models.ForeignKey(Cervejas,on_delete=models.PROTECT)
    analise_lote=models.IntegerField('Lote',default=0)
    analise_quantidade = models.IntegerField('Quantidade',default=0)
    conformidade=models.CharField(default='Conformidade',max_length=100,choices=conform_select)
    data_limite=models.DateField('Limite para Analise',default=date.today() + timedelta(days=30))
    status=models.CharField(default='Status',max_length=100,choices=status_select)


    def __str__(self):
        return self.analise_produto.rotulo

    class Meta:
        verbose_name='Analise'
        verbose_name_plural='Analises'
        ordering=['data_limite']
# Create your models here.

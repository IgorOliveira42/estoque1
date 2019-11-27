from django.db import models
from datetime import datetime,timedelta, date
from cidade.models import Cidades
from embalagem.models import Embalagens

conform_select=(('Conforme','Conforme'),('Não Conforme','Não Conforme'),)

class Cervejas(models.Model):
    rotulo=models.CharField('Rotulo',max_length=100)
    embalagem=models.ForeignKey(Embalagens, on_delete=models.PROTECT)
    lote=models.IntegerField('Lote',default=0)
    quantidade=models.IntegerField('Quantidade',default=0)
    fabric=models.DateField('Fabricação',auto_now=True)
    validade=models.DateField('Validade',default=date.today() + timedelta(days=180))
    conformidade=models.CharField(default='Conformidade',max_length=100,choices=conform_select)
    carga=models.DateField('Prazo para saída',default=date.today() + timedelta(days=20))
    
    def __str__(self):
        return self.rotulo

    class Meta:
        verbose_name='Cerveja'
        verbose_name_plural='Cervejas'
        ordering=['lote']


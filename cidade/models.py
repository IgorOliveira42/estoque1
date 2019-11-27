from django.db import models

class Cidades(models.Model):
    cidade = models.CharField('Cidade',max_length=100)

    def __str__(self):
        return self.cidade

    class Meta:
        verbose_name='Cidade'
        verbose_name_plural='Cidades'
        ordering=['cidade']

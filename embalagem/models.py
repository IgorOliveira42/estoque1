from django.db import models

class Embalagens(models.Model):
    embalagem = models.CharField('Embalagem',max_length=100)

    def __str__(self):
        return self.embalagem

    class Meta:
        verbose_name='Embalagem'
        verbose_name_plural='Embalagens'
        ordering=['embalagem']

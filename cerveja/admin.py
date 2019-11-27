from django.contrib import admin
from .models import Cervejas

class CervejasAdmin(admin.ModelAdmin):
    list_display=[
        'id','rotulo','embalagem','lote','fabric','validade','conformidade','carga'
        ]
    ordering=['id']

admin.site.register(Cervejas, CervejasAdmin)
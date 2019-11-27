from django.contrib import admin
from .models import Cidades

class CidadesAdmin(admin.ModelAdmin):
    list_display=[
        'id','cidade'
    ]
    ordering=['id']

admin.site.register(Cidades, CidadesAdmin)
from django.contrib import admin
from .models import Embalagens

class EmbalagensAdmin(admin.ModelAdmin):
    list_display=[
        'id','embalagem'
    ]
    ordering=['id']

admin.site.register(Embalagens, EmbalagensAdmin)
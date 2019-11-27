from django.contrib import admin
from .models import Generos

class GenerosAdmin(admin.ModelAdmin):
    list_display=[
        'id','genero'
        ]
    ordering=['id']
    search_fields=['genero']
    list_filter=['genero']

admin.site.register(Generos, GenerosAdmin)

# Register your models here.

from django.contrib import admin
from .models import Pessoa

class PessoaAdmin(admin.ModelAdmin):
    list_display = [
        'nome',
        'telefone',
        'idade',
    ]
    search_fields = [
        'nome'
    ]
    list_filter = [
        'idade'
    ]

admin.site.register(Pessoa, PessoaAdmin)
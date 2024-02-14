from django.contrib import admin
from coreapp.models import Aluno


@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    
    list_display = ['user','grupo_de_atendimento',]
    exclude = ['data_de_nascimento']
    readonly_fields = ['teve_covid_recentemente']
from django.contrib import admin
from coreapp.models import Aluno, Estabelecimento


@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    
    list_display = ['user','grupo_de_atendimento',]
    exclude = ['data_de_nascimento']
    readonly_fields = ['teve_covid_recentemente']
@admin.register(Estabelecimento)
class EstabelecimentoAdmin(admin.ModelAdmin):
    
    list_display = ['nome','co_cnes',]
    list_filter = ['nome', 'co_cnes',]
  
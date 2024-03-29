from django.db import models
from django.contrib.auth.models import User
import xml.etree.ElementTree as ET
import requests
from datetime import  datetime
# Create your models here.
class Estabelecimento(models.Model):
    co_cnes = models.CharField(max_length = 14 )
    nome = models.CharField(max_length = 100)

    def __str__(self):
        return f"{self.nome}, {self.co_cnes}"
    

class Aluno(models.Model):
    xml_url = "https://selecoes.lais.huol.ufrn.br/media/grupos_atendimento.xml"
    response = requests.get(xml_url)
    if response.status_code == 200:
        root = ET.fromstring(response.content)
        grupos = root.findall('.//grupoatendimento')
        opcoes = {}
        
        map = 0
        for grupo in grupos:
            map = map + 1
            opcoes[str(map)] = grupo.find('nome').text
        
    user = models.OneToOneField(User, on_delete=models.PROTECT,)

    nome_completo = models.CharField(max_length = 80 )
    data_de_nascimento = models.DateField()
    grupo_de_atendimento = models.CharField(
        choices = opcoes,
        max_length = 100
    )
    teve_covid_recentemente = models.BooleanField()

    def __str__(self):
        return self.nome_completo
class Agendamento(models.Model):
    estabelecimento = models.ForeignKey(Estabelecimento, on_delete = models.SET_NULL, null  =True)
    aluno = models.ForeignKey(Aluno, on_delete = models.PROTECT, )
    date = models.CharField( verbose_name  = "horário", max_length = 50)
        
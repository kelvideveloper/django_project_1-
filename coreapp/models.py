from django.db import models
from django.contrib.auth.models import User
import xml.etree.ElementTree as ET
import requests
# Create your models here.
class Estabelecimento(models.Model):
    co_unidade = models.CharField(max_length = 14 )
    co_unidade = models.CharField(max_length = 8)
    

class Aluno(models.Model):
    xml_url = "https://selecoes.lais.huol.ufrn.br/media/grupos_atendimento.xml"
    response = requests.get(xml_url)
    if response.status_code == 200:
        root = ET.fromstring(response.content)
        grupos = root.findall('.//grupoatendimento')
        opcoes = {'0':'Escolha uma opção',}
        
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
    
    
    
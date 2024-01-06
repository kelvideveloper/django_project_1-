from django.db import models
from django.contrib.auth.models import User
import xml.etree.ElementTree as ET
import requests
# Create your models here.

class Aluno(models.Model):
    xml_url = "https://selecoes.lais.huol.ufrn.br/media/grupos_atendimento.xml"
    response = requests.get(xml_url)
    if response.status_code == 200:
        root = ET.fromstring(response.content)
        grupos = root.findall('.//grupoatendimento')

        
        opcoes = [(grupo.find('codigo_si_pni').text, grupo.find('nome').text) for grupo in grupos]
      
    user = models.OneToOneField(User, on_delete=models.PROTECT,)
    nome = models.CharField(max_length = 80 )
    data_de_nascimento = models.DateField()
    grupo_de_atendimento = models.IntegerField(
        choices = opcoes,
    )

    def __str__(self):
        return self.nome
    
    
    
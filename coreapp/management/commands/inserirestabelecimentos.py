from django.core.management.base import BaseCommand, CommandError
from coreapp.models import Estabelecimento
import xml.etree.ElementTree as ET
import requests
class Command(BaseCommand):
    help = "Insere todos os estabelecimentos disponíveis no endereço 'https://selecoes.lais.huol.ufrn.br/media/estabelecimentos_pr.xml' "

    def handle(self, *args, **options):
       
            xml_url = "https://selecoes.lais.huol.ufrn.br/media/estabelecimentos_pr.xml"
            response = requests.get(xml_url)
            if response.status_code == 200:
                root = ET.fromstring(response.content)
                estabelecimentos = root.findall('.//estabelecimento')
            
                for estabelecimento in estabelecimentos:
                    
                    if not Estabelecimento.objects.filter(nome = estabelecimento.find('no_razao_social').text).exists():
                        atual = Estabelecimento.objects.create(
                            nome = estabelecimento.find('no_razao_social').text,
                            co_cnes = estabelecimento.find('co_cnes').text,
                            )  
                        atual.save()
                        self.stdout.write(
                        self.style.SUCCESS(f' estabelecimanto " {estabelecimento.find('no_razao_social').text} " adicionado com sucesso' )
                        )
                         
                   
                   
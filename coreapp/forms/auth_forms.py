from django import forms
from coreapp.models import Aluno
from datetime import  datetime
from django.contrib.auth.models import User
import xml.etree.ElementTree as ET
import requests
from utils.utils import validate_cpf 
class LoginForm(forms.Form):
    def clean_cpf(self):
        cpf = self.cleaned_data.get('cpf').replace('.', '' ).replace('-', '')
       
        if not validate_cpf(cpf):
            raise forms.ValidationError('Formato de cpf incorreto ou inválido')
        elif not User.objects.filter(username = cpf).exists():
            raise forms.ValidationError('Esse cpf não é cadastrado')
        return cpf
        
       
    cpf = forms.CharField(
        widget= forms.TextInput(
            attrs={
                'class': 'mask-cpf'
            }
        )
        )
    senha = forms.CharField(
        widget=forms.PasswordInput(),
        
    )
    

class SingUpForm(forms.ModelForm):
    cpf = forms.CharField(
        widget= forms.TextInput(
            attrs={
                'class': 'mask-cpf'
            }
        )
    )
    senha = forms.CharField(
        widget=forms.PasswordInput(),
        
    )
    senha2 = forms.CharField(
        label="confirmação de senha",
        widget=forms.PasswordInput(),
        
    )
    
    data_de_nascimento = forms.DateField(
        widget= forms.TextInput(
            attrs={
                'class': 'mask-date'
            }
        )
    )
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
        
            
       
    grupo_de_atendimento = forms.ChoiceField(
        choices= opcoes,
        widget=forms.Select(
        ),
        initial= '0'
            )
    teve_covid_recentemente = forms.ChoiceField(
        widget= forms.RadioSelect(
            attrs={
                'class': 'radio-button',
            }
        ),
        label="teve covid nos ultimos 30 dias ?",
        choices=[
            (True,"sim",),
            ( False,"não",)
        ]
    )
    class Meta:
        model =  Aluno
        fields = [
            'nome_completo',
            'data_de_nascimento',
            'grupo_de_atendimento',
            'teve_covid_recentemente',
        ]
    
    """ def clean_teve_covid_recentemente(self):
        resposta = self.cleaned_data.get('teve_covid_recentemente')
        if resposta:
            return resposta
        raise forms.ValidationError("você não pode participar se teve covid recentemente")
     """
    def clean_grupo_de_atendimento(self):
        data = self.cleaned_data["grupo_de_atendimento"]
        if data!= '0' :
            return data
        raise forms.ValidationError("Escolha uma das opções")
        
    
    def clean_cpf(self):
        cpf = self.cleaned_data.get('cpf').replace('.', '' ).replace('-', '')
       
        if not validate_cpf(cpf):
            raise forms.ValidationError('Informe um cpf válido')
        elif User.objects.filter(username = cpf).exists():
            raise forms.ValidationError('Um perfil com esse cpf já existe')
        return cpf
    
    def clean_data_de_nascimento(self):
        br_data = self.cleaned_data.get('data_de_nascimento')       
        today = datetime.today()
        born = datetime.strptime(str(br_data), '%Y-%m-%d').date()
        born_year = born.year
        born_day = born.day
        born_month = born.month
        this_year = today.year
        this_month = today.month
        this_day = today.day
        if this_year - born_year >= 1:
            valid =  True
        elif this_year - born_year == 0 and this_month > born_month:
            valid = True
        elif this_year - born_year == 0 and this_month == born_month and this_day >= born_day:
            valid = True
        else:
            valid = False
        if valid:
            return br_data
        else:
            raise forms.ValidationError('está data de nascimento não é possível')
      
        """ 
        if valid:
            return br_data
        else:
            raise forms.ValidationError('você precisa ter mais de 18 anos para criar uma conta')
      """
    
    

    def clean(self):
        cleaned_data = self.cleaned_data
        senha = cleaned_data.get('senha')
        senha2 = cleaned_data.get('senha2')
       
        if senha == senha2:
            
            return cleaned_data
        else:
            raise forms.ValidationError('as senhas precisam ser iguais')
    
                

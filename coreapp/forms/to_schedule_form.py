from django import forms
from coreapp.models import Agendamento, Aluno
from datetime import datetime, timedelta, date
import calendar
class ScheduleForm(forms.ModelForm):


    now = datetime.today().isoweekday()
    
    choices = {'':'---------'}
    map_day_names = {
        '0' : 'quarta-feira',
        '1' : 'quinta-feira',
        '2' : 'sexta-feira',
        '3' : 'sabado',
    }
    if now == 7 :
        
        next = date.today() + timedelta(days=3)     
        for i in range(4):
            
            choices[str(next)] = f'{map_day_names[str(i)]}, dia {next.strftime("%d/%m/%Y")} '
            next = next + timedelta(days=1)
    else:
        next = date.today() + timedelta(days=3-now)     
        for i in range(4):
            choices[str(next)] = f'{map_day_names[str(i)]}, dia {next.strftime("%d/%m/%Y")} '
            next = next + timedelta(days=1)
        
    date = forms.ChoiceField(
        label= "Data",
        choices= choices,
    )
    class Meta:
        model = Agendamento
        fields = [
            "estabelecimento",
            "date",
            
        ]
    def clean_date(self):
        data = self.cleaned_data["date"]
        if data!= '' :
            return data
        raise forms.ValidationError("Escolha uma das opções")
        
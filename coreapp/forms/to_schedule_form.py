from django import forms
from coreapp.models import Agendamento
from datetime import datetime, timedelta, date
import pytz
class ScheduleForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        age = kwargs.pop('age', None)
        super(ScheduleForm, self).__init__(*args, **kwargs)
        self.age = age

        now = datetime.today().isoweekday()
        choices = {'': '---------'}
        if age <= 29:
            horary = '13' 
        elif age <= 39:
            horary = '14'
        elif age <= 49:
            horary = '15'  
        elif age <= 59:
            horary = '16'
        else:
            horary = '17'
        self.horary = horary
        map_day_names = {
            '0': 'quarta-feira',
            '1': 'quinta-feira',
            '2': 'sexta-feira',
            '3': 'sábado',
        }
       
      
        if now == 7:
            next_date = date.today() + timedelta(days=3)
        else:
            next_date = date.today() + timedelta(days=3 - now)

        for i in range(4):
            choices[str(next_date.strftime("%d/%m/%Y"))] = f'{map_day_names[str(i)]}, dia {next_date.strftime("%d/%m/%Y")} às {horary}:00 horas '
            next_date = next_date + timedelta(days=1)

        self.fields['date'] = forms.ChoiceField(
            label="Data",
            choices=choices,
        )

    class Meta:
        model = Agendamento
        fields = [
            "estabelecimento",
            "date",
        ]
    def clean_date(self):
        data = self.cleaned_data["date"]
        age_horary =datetime.strptime(f'{self.horary}::00::00', '%H::%M::%S').time() 
        date_horary = datetime.strptime(data, '%d/%m/%Y').date()
        time_now =  datetime.now(pytz.timezone('America/Sao_Paulo')).time()
        
        today = date.today()
        
        if(today > date_horary ):
            raise forms.ValidationError("essa data já passou, escolha um horário futuro")
        elif today == date_horary:
            if time_now > age_horary:
                raise forms.ValidationError("Este horário não está mais disponível")
        return data
    

from django.shortcuts import render, redirect
from coreapp.forms import LoginForm, SingUpForm, ScheduleForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth import authenticate, login, logout
from coreapp.models import Aluno, Agendamento
from django.contrib.auth.models import User
from django.contrib import messages
from utils.utils import verify_age_is_more_than_18, verify_age
from datetime import  datetime, date
import pytz
@login_required(login_url="coreapp:home")
def agendar(request):
    user_data = Aluno.objects.get(user = request.user)
    agendamentos = Agendamento.objects.filter(aluno = user_data)
    today = datetime.today()
    born = user_data.data_de_nascimento
    idade = verify_age(born,today)
    if idade <= 29:
        horary = '13' 
    elif idade <= 39:
        horary = '14'
    elif idade <= 49:
        horary = '15'  
    elif idade <= 59:
        horary = '16'
    else:
        horary = '17'
    age_horary =datetime.strptime(f'{horary}::00::00', '%H::%M::%S').time()
    no_expireds = 0
    if agendamentos:
        today = date.today()
        for agendamento in agendamentos:
            data = agendamento.date[:10]
            date_day = datetime.strptime(data, '%d/%m/%Y').date()
            if today < date_day:
                no_expireds = 1
                break
            elif today == date_day:
                time_now =  datetime.now(pytz.timezone('America/Sao_Paulo')).time()
                if age_horary > time_now:
                    no_expireds = 1
                    break
    if no_expireds != 0:
        return redirect("coreapp:home")
    if not request.user.is_superuser:
        
        
        if idade < 18 or user_data.grupo_de_atendimento == "67" or user_data.grupo_de_atendimento == "70" or user_data.grupo_de_atendimento == "65" or user_data.teve_covid_recentemente:
            return redirect('coreapp:home')
        
        if request.method == 'POST':
            form = ScheduleForm(data=request.POST, age = idade)
            if form.is_valid():
                data = form.save(commit = False)
                date_day = form.cleaned_data.get("date")
                
                data.date_day = f"{date_day} às {horary}:00"
                data.aluno = Aluno.objects.get(user=request.user)
                data.save()
                messages.add_message(request, messages.SUCCESS, "Seu agendamento foi realizado com sucesso")
                return redirect("coreapp:home")
        else:
            form = ScheduleForm(age = idade)
    else:
        return render(request, 'coreapp/authentication_screen.html')
    
    context = {
        'form' : form,
        'form_action': '/agendar',
        'page': 'agendar exame'
    }
    return render( request, 'coreapp/form_screen.html',context)

def home(request):
    ...
    if request.user.is_authenticated and not request.user.is_superuser:
        
        ...
        user_data = Aluno.objects.get(user = request.user)
        today = datetime.today()
        born = user_data.data_de_nascimento
        if born is not None:
            esta_apto = True
            idade = verify_age(born,today)
            if idade < 18 or user_data.grupo_de_atendimento == "67" or user_data.grupo_de_atendimento == "70" or user_data.grupo_de_atendimento == "65" or user_data.teve_covid_recentemente:
                esta_apto = False
            
            context = {
                'user_data' : user_data,
                'idade' : idade,
                'esta_apto': esta_apto,
            }
        else:
            context = {
                'user_data' : user_data,
            }

        return render(request,'coreapp/home.html',context)
    else:
        return render(request, 'coreapp/authentication_screen.html')

def login_view(request):
    if request.user.is_authenticated and not request.user.is_superuser:
        return redirect("coreapp:home")

    if request.method == 'POST':
        
        form = LoginForm(data= request.POST)
        if form.is_valid():
            user = authenticate(
                request,
                username = form.cleaned_data.get('cpf'),
                password = form.cleaned_data.get('senha')    
            )
            if user is not None:
                login(request, user)

                return redirect("coreapp:home")


    else:
        form = LoginForm()
    context = {
        'form': form,
        'form_action': '/login',
        'page': 'Login' 
    }
    return render(request, 'coreapp/form_screen.html',context)

def cadastro_view(request):
    if request.user.is_authenticated:
        return redirect("coreapp:home")

    if request.method == 'POST':
        form = SingUpForm(data = request.POST)  
        if form.is_valid():     
            data = form.save(commit = False)
            cpf = form.cleaned_data.get('cpf')
            senha = form.cleaned_data.get('senha')
            user = User.objects.create_user(username=cpf,password=senha)
            user.save()
            data.user = user
            data.save()
            messages.add_message(request, messages.SUCCESS, "Seu Perfil foi criado com sucesso")
            today = datetime.today()
            br_data = form.cleaned_data.get('data_de_nascimento')
            born = datetime.strptime(str(br_data), '%Y-%m-%d').date()
            request.session['born'] = str(born)
            e_de_maior =verify_age_is_more_than_18(born,today)

            text = "você não está apto para a pesquisa pois:"
            if not e_de_maior:
                text = text + "Não tem 18 anos ou mais;"
            condition = form.cleaned_data.get('teve_covid_recentemente') == "True"
            if condition:
                text = text + " Teve covid recentemente;"
            if form.cleaned_data.get('grupo_de_atendimento') == "67" or form.cleaned_data.get('grupo_de_atendimento') == "70" or form.cleaned_data.get('grupo_de_atendimento') == "65":
                text = text + "É pertencente ao grupo " + form.opcoes[form.cleaned_data.get('grupo_de_atendimento')] + "."
            if text != "você não está apto para a pesquisa pois:":
                messages.add_message(request, messages.WARNING, text)
            return redirect('coreapp:login')
           
    else:
        form = SingUpForm()
    context = {
        'form': form,
        'form_action': '/cadastro',
        'page': 'Cadastro'

    }
    return render(request, 'coreapp/form_screen.html',context)

def termos(request):
    return render(request,"coreapp/termos.html", )

@login_required
def logout_view(request):
    logout(request)
    return redirect('coreapp:home')
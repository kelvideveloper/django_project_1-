from django.shortcuts import render, redirect
from coreapp.forms import LoginForm, SingUpForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth import authenticate, login, logout
from coreapp.models import Aluno
from django.contrib.auth.models import User
from django.contrib import messages
from utils.utils import verify_age_is_more_than_18, verify_age
from datetime import  datetime


def home(request):
    if request.user.is_authenticated:
        
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
    if request.user.is_authenticated:
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
        'url_action': '/login',
      
        
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
            if form.cleaned_data.get('teve_covid_recentemente'):
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
    }
    return render(request, 'coreapp/form_screen.html',context)

def termos(request):
    return render(request,"coreapp/termos.html", )

@login_required
def logout_view(request):
    logout(request)
    return redirect('coreapp:home')
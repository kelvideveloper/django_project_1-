from django.shortcuts import render, redirect
from coreapp.forms import LoginForm, SingUpForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth import authenticate, login, logout
from coreapp.models import Aluno
from django.contrib.auth.models import User


def home(request):
    if request.user.is_authenticated:
        return render(request,'coreapp/home.html')
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
from django.contrib import messages
import random
from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import views
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from .models import Cadastro, Citacao
# Create your views here.


def home(request):
    citacoes = Citacao.objects.all()
    if citacoes.exists():
        frase_aleatoria = random.choice(citacoes)
    else:
        frase_aleatoria = None 
    
    context = {
        'citacao': frase_aleatoria
    }
    
    return render(request, "telas_site/home.html", context)

def sobre(request):
    return render(request, "telas_site/sobre.html")

def equipe(request):
    return render(request, "telas_site/equipe.html")

def catalogo(request):
    return render(request, "telas_site/catalogo.html")

def grupos(request):
    return render(request, "telas_site/grupos.html")

def livro(request):
    return render(request, "telas_site/livro.html")

def inicial(request):
    return render(request,"telas_site/inicial.html")

def perfil(request):
    return render(request, "telas_site/perfil.html")

def caso(request):
    return render(request, "telas_site/caso.html")

def modelo(request):
    return render(request, "telas_site/modelos.html")

def cadastro(request):
    if request.method == 'GET':
        return render(request, "telas_site/cadastro.html")
    else:
        nome = request.POST.get("nome")
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        
        user = User.objects.filter(username=nome).exists()

        if user:
            messages.error(request, "Esse nome de usuário já está sendo usado!")
            return redirect('cadastro')
        
        user = User.objects.create_user(username=nome, email=email, password=senha)
        user.save()

        cadastro = Cadastro.objects.create(nome=nome, email=email, password=senha)
        cadastro.save()

        return redirect('home')

def login(request):
    if request.method == "GET":
        return render(request, "telas_site/login.html")
    else:
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        user = authenticate(email=email, password=senha)

        if user:
            login_django(request, user)
            return redirect('home')
        else:
            messages.error(request, "Esse nome de usuário já está sendo usado!")
            return redirect('login')
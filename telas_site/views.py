import random
from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import views
from django.contrib.auth.models import User
from .models import Citacao
# Create your views here.


def home(request):
    

    citacao = Citacao.objects.all()
    frase_aleatoria = random.choice(citacao) if mensagens.exists() else None
    context = {
        'frase': frase_aleatoria
    }

    return render(request, "telas_site/home.html")

def sobre(request):
    return render(request, "telas_site/sobre.html")

def equipe(request):
    return render(request, "telas_site/equipe.html")

def login(request):
    return render(request, "telas_site/login.html")

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
        username= request.POST.get("username")
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        user = User.objects.get(username=username)

        if user:
            return HttpResponse('Já existe um usuário com esse nome')

        return HttpResponse(username) 
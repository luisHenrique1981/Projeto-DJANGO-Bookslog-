from django.shortcuts import render
from django.http import HttpResponse
from . import views
# Create your views here.


def home(request):
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

def cadastro(request):
    if request.method == 'GET':
        return render(request, "telas_site/cadastro.html")
    else:
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        return HttpResponse(email)
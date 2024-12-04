from django.contrib import messages
import random
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from .models import Citacao, Usuario, Livro, Resenha
from .forms import CreateUserForm, LoginForm
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required

def home(request):
    citacoes = Citacao.objects.all()
    livros = Livro.objects.all()
    if citacoes.exists():
        frase_aleatoria = random.choice(citacoes)
    else:
        frase_aleatoria = None 
    
    context = {
        'citacao': frase_aleatoria,
        'livros': livros,
    }
    return render(request, "telas_site/home.html", context)

def detalhes_livro(request, id_livro):
    livro = get_object_or_404(Livro, id_livro=id_livro)
    resenhas = livro.resenhas.all() 
    context = {
        'livro': livro
    }
    return render(request, "telas_site/livro.html", context)

def lista_livro(request):
    return render(request, "telas_site/lista_livro.html")

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

def caso(request):
    return render(request, "telas_site/caso.html")

def modelo(request):
    return render(request, "telas_site/modelos.html")

def cadastro(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    context = {'registerform': form}
    return render(request, 'telas_site/cadastro.html', context=context)

def login(request):
    if request.user.is_authenticated:
        return redirect('home')
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('home')
            
    context = {'loginform': form}
    return render(request, 'telas_site/login.html', context=context)

def user_logout(request):
    auth_logout(request)
    return redirect('inicial')

def perfil(request):
    return render(request, "telas_site/perfil.html")

def buscar_livro(request):
    query = request.GET.get('q') 
    if query:
        try:
            livro = Livro.objects.get(titulo__iexact=query)
            return redirect('detalhes_livro', id_livro=livro.id_livro)
        except Livro.DoesNotExist:
            messages.error(request, "Livro não encontrado.")
            return redirect('catalogo') 
    return redirect('home')  


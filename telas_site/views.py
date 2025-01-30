import json
from django.utils import timezone
from datetime import datetime
from django.contrib import messages
import random
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, JsonResponse
from .models import Citacao, InteracaoLivro, StatusLeitura, Usuario, Livro, Resenha, InteracaoLivro
from .forms import CreateUserForm, LoginForm, ReviewForm, UserProfileForm
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.db.models import Avg, Count


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

def livro_detalhe(request, id_livro):
    livro = get_object_or_404(Livro, id_livro=id_livro)
    quantidade_resenhas = livro.resenhas.count()
    resenhas = livro.resenhas.all()

    status_counts = {
        'lidos': InteracaoLivro.objects.filter(livro=livro, status='lido').count(),
        'lendo': InteracaoLivro.objects.filter(livro=livro, status='lendo').count(),
        'quero_ler': InteracaoLivro.objects.filter(livro=livro, status='quero_ler').count(),
        'relendo': InteracaoLivro.objects.filter(livro=livro, status='relendo').count(),
        'larguei': InteracaoLivro.objects.filter(livro=livro, status='larguei').count(),
    }

    context = {
        'livro': livro,
        'resenhas': resenhas,
        'quantidade_resenhas': quantidade_resenhas,
        'status_counts': status_counts,
    }

    return render(request, "telas_site/livro.html", context)

def lista_livro(request):
    return render(request, "telas_site/lista_livro.html")

def sobre(request):
    return render(request, "telas_site/sobre.html")

def noticia(request):
    return render(request, "telas_site/noticia.html")

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

@login_required
def editar_perfil(request):
    usuario = request.user.usuario 

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=usuario)
        if form.is_valid():
            form.save() 
            return redirect('perfil') 
    else:
        form = UserProfileForm(instance=usuario)

    return render(request, 'perfil.html', {'form': form})

def perfil(request):
    user = request.user
    total_resenhas = Resenha.objects.filter(usuario=user).count()
    livros_lido = InteracaoLivro.objects.filter(usuario=request.user, status='lido').values('livro').distinct().count()
    livros_lendo = InteracaoLivro.objects.filter(usuario=request.user, status='lendo').values('livro').distinct().count()
    livros_quero_ler = InteracaoLivro.objects.filter(usuario=request.user, status='quero_ler').values('livro').distinct().count()
    livros_larguei = InteracaoLivro.objects.filter(usuario=request.user, status='largado').values('livro').distinct().count()
    livros_favorito = InteracaoLivro.objects.filter(usuario=request.user, status='favorito').values('livro').distinct().count()
    livros_relendo = InteracaoLivro.objects.filter(usuario=request.user, status='relendo').values('livro').distinct().count()

    livros = Livro.objects.all()


    context = {
        'total_resenhas': total_resenhas,
        'livros_lido': livros_lido,
        'livros_lendo': livros_lendo,
        'livros_quero_ler': livros_quero_ler,
        'livros_larguei': livros_larguei,
        'livros_favorito': livros_favorito,
        'livros_relendo': livros_relendo,
        'livros': livros 
    }

    return render(request, "telas_site/perfil.html", context)


def detalhe_livro(request, livro_id):
    livro = Livro.objects.get(id_livro=livro_id)
    
    lendo_count = InteracaoLivro.objects.filter(livro=livro, status='lendo').count()
    lido_count = InteracaoLivro.objects.filter(livro=livro, status='lido').count()
    quero_ler_count = InteracaoLivro.objects.filter(livro=livro, status='quero_ler').count()
    favorito_count = InteracaoLivro.objects.filter(livro=livro, status='favorito').count()
    relendo_count = InteracaoLivro.objects.filter(livro=livro, status='relendo').count()
    larguei_count = InteracaoLivro.objects.filter(livro=livro, status='larguei').count()

    media_avaliacoes = livro.media_avaliacoes()
    
    context = {
        'livro': livro,
        'lendo_count': lendo_count,
        'lido_count': lido_count,
        'quero_ler_count': quero_ler_count,
        'favorito_count': favorito_count,
        'relendo_count': relendo_count,
        'larguei_count': larguei_count,
        'media_avaliacoes': media_avaliacoes,
    }

    return render(request, 'livro/detalhes.html', context)

@receiver(post_save, sender=Resenha)
@receiver(post_delete, sender=Resenha)
def atualizar_resenhas_usuario(sender, instance, **kwargs):
    usuario = instance.usuario
    total_resenhas = Resenha.objects.filter(usuario=usuario).count()
    Usuario.objects.filter(user=usuario).update(resenhas_usuario=total_resenhas)

@login_required
def submit_review(request, book_id):
    livro = get_object_or_404(Livro, id_livro=book_id)
    if request.method == 'POST':
        titulo_resenha = request.POST.get('titulo_resenha')
        texto_resenha = request.POST.get('texto_resenha')
        nota_resenha = request.POST.get('nota_resenha')

        if nota_resenha and nota_resenha.isdigit():
            nota_resenha = int(nota_resenha)
        else:
            nota_resenha = None

        if titulo_resenha and texto_resenha and nota_resenha:
            if not Resenha.objects.filter(
                livro=livro,
                usuario=request.user,
                titulo_resenha=titulo_resenha
            ).exists():
                resenha = Resenha.objects.create(
                    livro=livro,
                    usuario=request.user,
                    titulo_resenha=titulo_resenha,
                    texto_resenha=texto_resenha,
                    nota_resenha=nota_resenha,
                )
                resenha.save()
                messages.success(request, "Resenha criada com sucesso!")
            else:
                messages.warning(request, "Você já enviou uma resenha com este título para este livro.")
            return redirect('detalhes_livro', id_livro=livro.id_livro)

    messages.error(request, "Por favor, preencha todos os campos.")
    return redirect('detalhes_livro', id_livro=livro.id_livro)

@login_required
def delete_review(request, review_id):
    resenha = get_object_or_404(Resenha, id=review_id, usuario=request.user)
    resenha.delete()
    messages.success(request, "Resenha excluída com sucesso!")
    return redirect('detalhes_livro', id_livro=resenha.livro.id_livro)

@login_required
@csrf_exempt
def interagir_livro(request, id_livro, status):
    if request.method == 'POST':
        try:
            livro = Livro.objects.get(id_livro=id_livro)

            interacao, created = InteracaoLivro.objects.update_or_create(
                livro=livro,
                usuario=request.user,
                defaults={'status': status, 'data_interacao': timezone.now()},
            )

            return JsonResponse({'success': True, 'message': 'Interação salva com sucesso!'})
        except Livro.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'Livro não encontrado.'}, status=404)
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)}, status=500)

    return JsonResponse({'success': False, 'message': 'Método não permitido.'}, status=405)

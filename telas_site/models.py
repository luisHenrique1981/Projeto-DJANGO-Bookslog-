from decimal import Decimal
from django.dispatch import receiver
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
from django.db.models import Avg
from django.db.models.signals import post_save, post_delete

        
class Livro(models.Model):
    id_livro = models.AutoField(primary_key=True)
    autor = models.CharField(max_length=100)
    capa = models.ImageField(null=True, blank=True)
    sinopse = models.CharField(max_length=350)
    data_publicacao = models.TextField(max_length=80)
    genero = models.TextField(max_length=80)
    quantidade_paginas = models.TextField(max_length=80)
    titulo = models.CharField(max_length=100)
    editora = models.TextField()
    idioma = models.TextField()
    classificacao_indicativa = models.TextField()
    foto_autor = models.ImageField(null=True, blank=True)
    bio_autor = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.titulo
    
    def media_avaliacoes(self):
        media = self.resenhas.aggregate(media=Avg('nota_resenha'))['media']
        
        if media is None:
            return "Sem avaliações" 

        return round(Decimal(media), 2)

class Resenha(models.Model):
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE, related_name='resenhas') 
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    titulo_resenha = models.CharField(max_length=200)
    texto_resenha = models.TextField()
    nota_resenha = models.PositiveSmallIntegerField(choices=[(i, i) for i in range(1, 6)])
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return f'Resenha de {self.usuario.username} sobre {self.livro.titulo}'

class Pesquisa(models.Model):
    genero = models.TextField()
    editora = models.TextField()
    autor = models.TextField()
    titulo_livro = models.TextField()
    pesquisa_id = models.AutoField(primary_key=True)

class Grupo(models.Model):
    nome = models.CharField(max_length=50)
    quantidade_usuario = models.IntegerField()
    descricao = models.CharField(max_length=100)
    administradores = models.IntegerField()
    grupo_id = models.AutoField(primary_key=True)

class Lista(models.Model):
    nome = models.CharField(max_length=50)
    quantidade_livros = models.IntegerField()
    descricao = models.CharField(max_length=100)
    lista_id = models.AutoField(primary_key=True)

class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    nome = models.CharField(max_length=60)
    descricao = models.CharField(max_length=100)
    lendo_atualmente = models.IntegerField(null=True, blank=True)
    pretende_ler = models.IntegerField(null=True, blank=True)
    lidos = models.IntegerField(null=True, blank=True)
    favoritos = models.IntegerField(null=True, blank=True)
    quantidade_seguidores = models.IntegerField(null=True, blank=True)
    quantidade_seguindo = models.IntegerField(null=True, blank=True)
    imagem_perfil = models.ImageField(null=True, blank=True)
    resenhas_usuario = models.IntegerField(null=True, blank=True)
    id_usuario = models.AutoField(primary_key=True)
    grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE,  null=True, blank=True)
    lista = models.ForeignKey(Lista, on_delete=models.CASCADE, null=True, blank=True)

class Usuario_has_Pesquisa(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    resenha = models.ForeignKey(Resenha, on_delete=models.CASCADE)
    pesquisa = models.ForeignKey(Pesquisa, on_delete=models.CASCADE)

class Citacao(models.Model):
    titulo = models.TextField()
    frase = models.TextField()
    imagem = models.ImageField()

    def __str__(self):
        return self.titulo
    
class InteracaoLivro(models.Model):
    STATUS_CHOICES = [
        ('lido', 'Lido'),
        ('lendo', 'Lendo'),
        ('quero_ler', 'Quero Ler'),
        ('favorito', 'Favorito'),
        ('relendo', 'Relendo'),
        ('larguei', 'Larguei'),
    ]
    
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)  
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    data_interacao = models.DateTimeField(default=timezone.now) 

    class Meta:
        unique_together = ('livro', 'usuario')  

    def __str__(self):
        return f'{self.usuario.username} - {self.livro.titulo} - {self.status}'

class Review(models.Model):
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    rating = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

class StatusLeitura(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE)  
    status = models.CharField(max_length=20, choices=[
        ('lido', 'Lido'),
        ('lendo', 'Lendo'),
        ('quero_ler', 'Quero Ler'),
        ('favorito', 'Favorito'),
        ('relendo', 'Relendo'),
        ('larguei', 'Larguei'),
    ])
    data_atualizacao = models.DateTimeField(auto_now=True)
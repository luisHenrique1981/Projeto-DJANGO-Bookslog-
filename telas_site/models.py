from django.db import models
from django.contrib.auth.models import User

class Resenha(models.Model):
    texto_resenha = models.CharField(max_length=500)
    foto_usuario = models.ImageField(null=True, blank=True)
    nota_resenha = models.DecimalField(max_digits=5, decimal_places=1)
    titulo_resenha = models.CharField(max_length=100)
    data_resenha = models.DateTimeField(auto_now_add=True)
    id_resenha = models.AutoField(primary_key=True)
    id_livro = models.ForeignKey('Livro', on_delete=models.CASCADE, related_name='resenhas', null=True, blank=True)
    usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE, related_name='resenhas', null=True, blank=True)

class Livro(models.Model):
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
    id_livro = models.AutoField(primary_key=True)

    def __str__(self):
        return self.titulo

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

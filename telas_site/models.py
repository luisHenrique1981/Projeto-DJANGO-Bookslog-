from django.db import models

# Create your models here.
class Cadastro(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    cadastro_usuario_id = models.AutoField(primary_key=True)

    def __str__(self):
        return self.nome

class Resenha(models.Model):
    texto_resenha = models.CharField(max_length=500)
    nota_resenha = models.IntegerField()
    titulo_resenha = models.CharField(max_length=100)
    data_resenha = models.DateTimeField(auto_now_add=True)
    id_resenha = models.AutoField(primary_key=True)

class Livro(models.Model):
    autor = models.CharField(max_length=100)
    data_publicacao = models.DateField()
    genero = models.TextField()
    sinopse = models.CharField(max_length=200)
    quantidade_paginas = models.IntegerField()
    titulo = models.CharField(max_length=100)
    editora = models.TextField()
    idioma = models.TextField()
    classificacao_indicativa = models.TextField()
    resenhas = models.IntegerField()
    id_livro = models.AutoField(primary_key=True)
    resenha = models.ForeignKey(Resenha, on_delete=models.CASCADE)

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
    nome = models.CharField(max_length=60)
    descricao = models.CharField(max_length=100)
    lendo_atualmente = models.IntegerField()
    pretende_ler = models.IntegerField()
    lidos = models.IntegerField()
    favoritos = models.IntegerField()
    quantidade_seguidores = models.IntegerField()
    quantidade_seguindo = models.IntegerField()
    imagem_perfil = models.ImageField()
    resenhas_usuario = models.IntegerField()
    id_usuario = models.AutoField(primary_key=True)
    cadastro = models.ForeignKey(Cadastro, on_delete=models.CASCADE)
    resenha = models.ForeignKey(Resenha, on_delete=models.CASCADE)
    grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE)
    lista = models.ForeignKey(Lista, on_delete=models.CASCADE)

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

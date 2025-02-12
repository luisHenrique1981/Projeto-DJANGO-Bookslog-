# Generated by Django 5.0.4 on 2025-01-09 19:24

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Citacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.TextField()),
                ('frase', models.TextField()),
                ('imagem', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Grupo',
            fields=[
                ('nome', models.CharField(max_length=50)),
                ('quantidade_usuario', models.IntegerField()),
                ('descricao', models.CharField(max_length=100)),
                ('administradores', models.IntegerField()),
                ('grupo_id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Lista',
            fields=[
                ('nome', models.CharField(max_length=50)),
                ('quantidade_livros', models.IntegerField()),
                ('descricao', models.CharField(max_length=100)),
                ('lista_id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Livro',
            fields=[
                ('id_livro', models.AutoField(primary_key=True, serialize=False)),
                ('autor', models.CharField(max_length=100)),
                ('capa', models.ImageField(blank=True, null=True, upload_to='')),
                ('sinopse', models.CharField(max_length=350)),
                ('data_publicacao', models.TextField(max_length=80)),
                ('genero', models.TextField(max_length=80)),
                ('quantidade_paginas', models.TextField(max_length=80)),
                ('titulo', models.CharField(max_length=100)),
                ('editora', models.TextField()),
                ('idioma', models.TextField()),
                ('classificacao_indicativa', models.TextField()),
                ('foto_autor', models.ImageField(blank=True, null=True, upload_to='')),
                ('bio_autor', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pesquisa',
            fields=[
                ('genero', models.TextField()),
                ('editora', models.TextField()),
                ('autor', models.TextField()),
                ('titulo_livro', models.TextField()),
                ('pesquisa_id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Resenha',
            fields=[
                ('titulo_resenha', models.CharField(max_length=200)),
                ('texto_resenha', models.TextField()),
                ('nota_resenha', models.PositiveSmallIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('livro', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='resenhas', to='telas_site.livro')),
                ('usuario', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('rating', models.PositiveIntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('livro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='telas_site.livro')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('nome', models.CharField(max_length=60)),
                ('descricao', models.CharField(max_length=100)),
                ('lendo_atualmente', models.IntegerField(blank=True, null=True)),
                ('pretende_ler', models.IntegerField(blank=True, null=True)),
                ('lidos', models.IntegerField(blank=True, null=True)),
                ('favoritos', models.IntegerField(blank=True, null=True)),
                ('quantidade_seguidores', models.IntegerField(blank=True, null=True)),
                ('quantidade_seguindo', models.IntegerField(blank=True, null=True)),
                ('imagem_perfil', models.ImageField(blank=True, null=True, upload_to='')),
                ('resenhas_usuario', models.IntegerField(blank=True, null=True)),
                ('id_usuario', models.AutoField(primary_key=True, serialize=False)),
                ('grupo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='telas_site.grupo')),
                ('lista', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='telas_site.lista')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='InteracaoLivro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('quero_ler', 'Quero Ler'), ('lendo', 'Lendo'), ('lido', 'Lido'), ('larguei', 'Larguei'), ('relendo', 'Relendo')], default='quero_ler', max_length=20)),
                ('favorito', models.BooleanField(default=False)),
                ('livro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='interacoes', to='telas_site.livro')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='interacoes', to='telas_site.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario_has_Pesquisa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pesquisa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='telas_site.pesquisa')),
                ('resenha', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='telas_site.resenha')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='telas_site.usuario')),
            ],
        ),
    ]

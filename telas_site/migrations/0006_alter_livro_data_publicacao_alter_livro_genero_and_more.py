# Generated by Django 5.0.4 on 2024-10-17 01:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('telas_site', '0005_remove_livro_resenhas_alter_livro_genero'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livro',
            name='data_publicacao',
            field=models.TextField(max_length=80),
        ),
        migrations.AlterField(
            model_name='livro',
            name='genero',
            field=models.TextField(max_length=80),
        ),
        migrations.AlterField(
            model_name='livro',
            name='quantidade_paginas',
            field=models.TextField(max_length=80),
        ),
        migrations.AlterField(
            model_name='livro',
            name='sinopse',
            field=models.TextField(max_length=80),
        ),
    ]

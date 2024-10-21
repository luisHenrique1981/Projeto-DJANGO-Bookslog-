# Generated by Django 5.0.4 on 2024-10-13 20:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('telas_site', '0003_remove_usuario_cadastro_delete_cadastro'),
    ]

    operations = [
        migrations.AddField(
            model_name='livro',
            name='capa',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='livro',
            name='resenha',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='livros', to='telas_site.resenha'),
        ),
    ]
# Generated by Django 5.0.4 on 2024-10-13 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('telas_site', '0004_livro_capa_alter_livro_resenha'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='livro',
            name='resenhas',
        ),
        migrations.AlterField(
            model_name='livro',
            name='genero',
            field=models.TextField(max_length=20),
        ),
    ]

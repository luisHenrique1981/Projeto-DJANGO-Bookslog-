# Generated by Django 5.0.4 on 2025-01-11 00:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('telas_site', '0004_alter_interacaolivro_data_interacao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interacaolivro',
            name='status',
            field=models.CharField(choices=[('lido', 'Lido'), ('lendo', 'Lendo'), ('quero_ler', 'Quero Ler'), ('larguei', 'Larguei'), ('favorito', 'Favorito'), ('relendo', 'Relendo'), ('larguei', 'Larguei')], max_length=10),
        ),
    ]

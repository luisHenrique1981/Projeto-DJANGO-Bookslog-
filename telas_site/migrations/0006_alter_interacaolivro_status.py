# Generated by Django 5.0.4 on 2025-01-20 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('telas_site', '0005_alter_interacaolivro_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interacaolivro',
            name='status',
            field=models.CharField(choices=[('lido', 'Lido'), ('lendo', 'Lendo'), ('quero_ler', 'Quero Ler'), ('favorito', 'Favorito'), ('relendo', 'Relendo'), ('larguei', 'Larguei')], max_length=10),
        ),
    ]

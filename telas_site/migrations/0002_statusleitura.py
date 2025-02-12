# Generated by Django 5.0.4 on 2025-01-10 21:56

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('telas_site', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='StatusLeitura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('lido', 'Lido'), ('lendo', 'Lendo'), ('quero_ler', 'Quero Ler'), ('favorito', 'Favorito'), ('relendo', 'Relendo'), ('larguei', 'Larguei')], max_length=20)),
                ('data_atualizacao', models.DateTimeField(auto_now=True)),
                ('livro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='telas_site.livro')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

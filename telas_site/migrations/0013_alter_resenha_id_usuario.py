# Generated by Django 5.0.4 on 2024-10-17 11:45

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('telas_site', '0012_alter_resenha_nota_resenha'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='resenha',
            name='id_usuario',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='avaliacoes', to=settings.AUTH_USER_MODEL),
        ),
    ]

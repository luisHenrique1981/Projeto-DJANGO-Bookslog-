# Generated by Django 5.0.4 on 2024-10-18 17:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('telas_site', '0017_remove_resenha_id_usuario_resenha_usuario_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='resenha',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='usuarios', to='telas_site.resenha'),
        ),
    ]

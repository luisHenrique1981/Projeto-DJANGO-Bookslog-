# Generated by Django 5.0.4 on 2024-10-18 17:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('telas_site', '0019_alter_usuario_grupo_alter_usuario_lista'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='grupo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='telas_site.grupo'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='lista',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='telas_site.lista'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='resenha',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='usuarios', to='telas_site.resenha'),
        ),
    ]

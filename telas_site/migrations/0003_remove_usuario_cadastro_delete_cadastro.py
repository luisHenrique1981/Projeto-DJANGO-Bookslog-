# Generated by Django 5.0.4 on 2024-10-08 12:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('telas_site', '0002_citacao'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='cadastro',
        ),
        migrations.DeleteModel(
            name='Cadastro',
        ),
    ]

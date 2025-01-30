from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Usuario

@receiver(post_save, sender=User)
def criar_usuario_perfil(sender, instance, created, **kwargs):
    if created:
        Usuario.objects.create(user=instance, nome=instance.username, imagem_perfil='media/default.jpg')

@receiver(post_save, sender=User)
def salvar_usuario_perfil(sender, instance, **kwargs):
    instance.usuario.save()

from django.contrib import admin
from .models import Usuario, Livro, Resenha, Pesquisa, Lista, Grupo, Usuario_has_Pesquisa, Citacao

# Register your models here.

admin.site.register(Usuario)
admin.site.register(Livro)
admin.site.register(Resenha)
admin.site.register(Pesquisa)
admin.site.register(Lista)
admin.site.register(Grupo)
admin.site.register(Usuario_has_Pesquisa)
admin.site.register(Citacao)
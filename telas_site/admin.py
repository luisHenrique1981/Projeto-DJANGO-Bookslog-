from django.contrib import admin
from .models import Usuario, Livro, Resenha, Pesquisa, Lista, Grupo, Cadastro, Usuario_has_Pesquisa

# Register your models here.

admin.site.register(Usuario)
admin.site.register(Livro)
admin.site.register(Resenha)
admin.site.register(Pesquisa)
admin.site.register(Lista)
admin.site.register(Grupo)
admin.site.register(Cadastro)
admin.site.register(Usuario_has_Pesquisa)
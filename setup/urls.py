"""
URL configuration for setup project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static 
from django.views.generic import RedirectView

from telas_site import views
from telas_site.views import home, lista_livro
from telas_site.views import sobre
from telas_site.views import equipe
from telas_site.views import catalogo
from telas_site.views import login
from telas_site.views import cadastro 
from telas_site.views import livro
from telas_site.views import inicial
from telas_site.views import perfil
from telas_site.views import caso
from telas_site.views import modelo

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home, name='home'),
    path('sobre/', views.sobre, name='sobre'),
    path('equipe/', views.equipe, name='equipe'),
    path('catalogo/', views.catalogo, name='catalogo'),
    path('login/', views.login, name='login'),
    path('user-logout', views.user_logout, name='user-logout'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('grupos/',views.grupos, name='grupos'),
    path('livro/', views.livro, name='livro'),
    path('livro/<int:id_livro>/', views.livro_detalhe, name='detalhes_livro'),
    path("inicial/",views.inicial, name='inicial'),
    path("perfil/", views.perfil, name='perfil'),
    path('editar-perfil/', views.editar_perfil, name='editar_perfil'),
    path('caso/', views.caso, name='caso'),
    path('modelo/', views.modelo, name='modelo'),
    path('', include('telas_site.urls')),
    path('buscar/', views.buscar_livro, name='buscar_livro'),
    path('livro/<int:book_id>/resenha/', views.submit_review, name='submit_review'),
    path('delete_review/<int:review_id>/', views.delete_review, name='delete_review'),
    path('livro/<int:id_livro>/interagir/<str:status>/', views.interagir_livro, name='interagir_livro'),
    path('favicon.ico', RedirectView.as_view(url='/static/img/favicon.ico', permanent=True)),
    path('noticia/', views.noticia, name='noticia'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
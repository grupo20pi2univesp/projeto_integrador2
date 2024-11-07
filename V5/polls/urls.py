from django.urls import path

#importando views na polls
from polls.views import index, sobre, voluntario, doacoes, equipe, ajude, noticias,atendidos,newsletter,infouteis

#criando lista de caminhos para as views

urlpatterns = [ 
    path('index', index, name="index"),
    path('noticias', noticias, name="noticias"),
    path('sobre', sobre, name="sobre"),
    path('equipe', equipe, name="equipe"),
    path('doacoes', doacoes, name="doacoes"),
    path('voluntario', voluntario, name="voluntario"),
    path('atendidos', atendidos, name="atendidos"),
    path('ajude', ajude, name="ajude"),
    path('newsletter', newsletter, name="newsletter"),
    path('infouteis', infouteis, name="infouteis"),
    path('', index, name='index'),
]

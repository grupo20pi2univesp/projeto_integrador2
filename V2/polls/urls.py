from django.urls import path

#importando views na polls
from polls.views import index, sobre, voluntario, doacoes_necessarias, equipe, ajude

#criando lista de caminhos para as views

urlpatterns = [ 
    path('index', index, name="index"),
    path('sobre', sobre, name="sobre"),
    path('equipe', equipe, name="equipe"),
    path('doacoes_necessarias', doacoes_necessarias, name="doacoes_necessarias"),
    path('voluntario', voluntario, name="voluntario"),
    path('ajude', ajude, name="ajude"),
    path('', index, name='index'),

]

from django.shortcuts import render,redirect
from django import forms
from .models import *
from django.http import HttpResponse
from polls.forms import doacaoforms,voluntarioforms


# Define view de teste baseada em função (rotina para executar)
def index(request):
    return render (request, 'index.html')

#views para o frame polls/views.py
def sobre(request):
    return render (request, 'sobre.html')

def equipe(request):
    return render (request, 'equipe.html')

def doacoes_necessarias(request):
    
    doacoes = doacao_cadastro.objects.all()

    if request.method == 'GET':
        
        form = doacaoforms()

        context = {
            'form': form,
        }

        return render(request, 'doacoes_necessarias.html', {'form': form,'doacoes': doacoes})
    
    else:

        form = doacaoforms(request.POST)

        if form.is_valid():

            form.save()
            form = doacaoforms()
    
        context = {
            'form': form,
            }

        return render(request, 'doacoes_necessarias.html', {'form': form,'doacoes': doacoes})
    
def voluntario(request):
     
     voluntarios = voluntario_cadastro.objects.all()

     if request.method == 'GET':
        
        form = voluntarioforms()

        context = {
            'form': form,
        }

        return render(request, 'voluntario.html', {'form': form, 'voluntarios': voluntarios})
    
     else:

        form = voluntarioforms(request.POST)

        if form.is_valid():

            form.save()
            form = voluntarioforms()
    
        context = {
            'form': form,
            }
        
        return render(request, 'voluntario.html', {'form': form, 'voluntarios': voluntarios})

def ajude(request):
    return render (request, 'ajude.html')
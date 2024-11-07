from django.shortcuts import render,redirect
from django import forms
from .models import *
from django.http import HttpResponse
from polls.forms import doacaoforms,voluntarioforms,atendidosforms,newsletterforms

# Define view de teste baseada em função (rotina para executar)
def index(request):
    return render (request, 'index.html')

#views para o frame polls/views.py
def noticias(request):
    return render (request, 'noticias.html')

#views para o frame polls/views.py
def sobre(request):
    return render (request, 'sobre.html')

def equipe(request):
    return render (request, 'equipe.html')

def doacoes(request):
    
    doacoes = doacao_cadastro.objects.all()

    if request.method == 'GET':
        
        form = doacaoforms()

        context = {
            'form': form,
        }

        return render(request, 'doacoes.html', {'form': form,'doacoes': doacoes})
    
    else:

        form = doacaoforms(request.POST)

        if form.is_valid():

            form.save()
            form = doacaoforms()
    
        context = {
            'form': form,
            }

        return render(request, 'doacoes.html', {'form': form,'doacoes': doacoes})
    
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

def atendidos(request):
         
    atendidos = atendidos_cadastro.objects.all()

    if request.method == 'GET':
        
        form = atendidosforms()

        context = {
            'form': form,
        }

        return render(request, 'atendidos.html', {'form': form, 'atendidos': atendidos})
    
    else:

        form = atendidosforms(request.POST)

        if form.is_valid():

            form.save()
            form = atendidosforms()
    
        context = {
            'form': form,
            }
        
        return render(request, 'atendidos.html', {'form': form, 'atendidos': atendidos})

    return render (request, 'atendidos.html')

def ajude(request):
    return render (request, 'ajude.html')

def newsletter(request):

    newsletter = newsletter_cadastro.objects.all()

    if request.method == 'GET':
        
        form = newsletterforms()

        context = {
            'form': form,
        }

        return render(request, 'newsletter.html', {'form': form, 'newsletter': newsletter})
    
    else:

        form = newsletterforms(request.POST)

        if form.is_valid():

            form.save()
            form = newsletterforms()
    
        context = {
            'form': form,
            }
        
        return render(request, 'newsletter.html', {'form': form, 'newsletter': newsletter})

    return render (request, 'newsletter.html')

def infouteis(request):
    return render (request, 'infouteis.html')
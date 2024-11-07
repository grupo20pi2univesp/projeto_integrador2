from django import forms
from .models import *

class doacaoforms(forms.ModelForm):
    class Meta:
        model = doacao_cadastro
        fields = '__all__'

class voluntarioforms(forms.ModelForm):
    class Meta:
        model = voluntario_cadastro
        fields = '__all__'

class atendidosforms(forms.ModelForm):
    class Meta:
        model = atendidos_cadastro
        fields = '__all__'

class newsletterforms(forms.ModelForm):
    class Meta:
        model = newsletter_cadastro
        fields = '__all__'
from django.contrib import admin

from. models import doacao_cadastro, voluntario_cadastro, atendidos_cadastro, newsletter_cadastro

admin.site.register(doacao_cadastro)
admin.site.register(voluntario_cadastro)
admin.site.register(atendidos_cadastro)
admin.site.register(newsletter_cadastro)


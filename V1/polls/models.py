from django.db import models

class doacao_cadastro(models.Model):
    Item_Necessario = models.CharField(max_length=100, null=True)
    Quantidade_Necessaria = models.CharField(max_length=100, null=True)
    Data_Limite_para_Doacao = models.DateField(blank=True, null=True)
    Voluntario_Responsavel_pela_Captacao = models.CharField(max_length=100, null=True)
    Contato = models.CharField(max_length=11, blank=True, null=True)
    Email = models.EmailField(blank=True, null=True)
    
    def __str__(self):
        return self.Item_Necessario

class voluntario_cadastro(models.Model):
    nome_do_voluntario = models.CharField(max_length=300, null=True)
    data_de_nascimento = models.DateField(blank=True, null=True)
    Endereco = models.CharField(max_length=300, null=True)
    Email = models.EmailField(blank=True, null=True)
    Celular = models.CharField(max_length=20, blank=True, null=True)
    Dias_disponiveis_para_atuar = models.TextField(default='')
    Atividades_que_gostaria_de_executar = models.TextField(default='')
    
    def __str__(self):
        return self.nome_do_voluntario
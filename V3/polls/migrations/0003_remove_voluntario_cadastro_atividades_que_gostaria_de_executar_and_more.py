# Generated by Django 5.0.3 on 2024-05-13 20:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_remove_doacao_cadastro_celular_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='voluntario_cadastro',
            name='Atividades_que_gostaria_de_executar',
        ),
        migrations.RemoveField(
            model_name='voluntario_cadastro',
            name='Celular',
        ),
        migrations.RemoveField(
            model_name='voluntario_cadastro',
            name='Data_de_nascimento',
        ),
        migrations.RemoveField(
            model_name='voluntario_cadastro',
            name='Dias_disponiveis_para_atuar',
        ),
        migrations.RemoveField(
            model_name='voluntario_cadastro',
            name='Email',
        ),
        migrations.RemoveField(
            model_name='voluntario_cadastro',
            name='Endereco',
        ),
    ]

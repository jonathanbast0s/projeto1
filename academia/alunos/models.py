# makemigrations: Analisa as alterações feitas nos arquivos 
# models.py e cria arquivos de "projeto" (histórico) na pasta 
# migrations/. Ele não altera o banco de dados diretamente, apenas 
# gera os scripts que descrevem o que deve ser alterado.

# migrate: Pega esses arquivos de migração pendentes e executa 
# os comandos SQL no banco de dados de fato, criando ou alterando 
# as tabelas.

from django.db import models

class Aluno(models.models.Model if hasattr(models, 'models') else models.Model):
    nome = models.CharField(max_length=100)
    matricula = models.CharField(max_length=20, unique=True)
    curso = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
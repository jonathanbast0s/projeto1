from django.db import models

class Pessoa(models.Model):

    nome = models.CharField(max_length=200)

    telefone = models.CharField(max_length=11)

    idade = models.IntegerField(null=True)

    def __str__(self):
        return self.nome

class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    idade = models.IntegerField()
    cidade = models.CharField(max_length=50)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    estoque = models.IntegerField()
    categoria = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nome} - R$ {self.preco}"

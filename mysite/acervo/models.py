from django.db import models
from datetime import date
from django.contrib.auth.models import User

class Item(models.Model):
    nome = models.CharField(max_length = 50)
    descricao = models.CharField(max_length = 100, blank = True)
    emprestado = models.BooleanField()
    user = models.ForeignKey(User, on_delete = models.CASCADE, default = None)

    def __str__(self):
        return self.nome

class Livro(models.Model):
    titulo = models.CharField(max_length = 100)
    autor = models.CharField(max_length = 50)
    ano = models.IntegerField()
    emprestado = models.BooleanField()
    user = models.ForeignKey(User, on_delete = models.CASCADE, default = None)

    def __str__(self):
       return self.titulo

class Contato(models.Model):
    nome_cont = models.CharField(max_length = 50)
    email = models.CharField(max_length = 50)
    telefone = models.CharField(max_length = 15)
    user = models.ForeignKey(User, on_delete = models.CASCADE, default = None)

    def __str__(self):
        return self.nome_cont

class Emprestimo(models.Model):
    data_emp = models.DateField(default = date.today)
    data_dev = models.DateField(blank = True, null = True)
    item = models.ForeignKey(Item, on_delete = models.CASCADE, null = True, blank = True)
    livro = models.ForeignKey(Livro, on_delete = models.CASCADE, null = True, blank = True)
    contato = models.ForeignKey(Contato, on_delete = models.CASCADE)
    user = models.ForeignKey(User, on_delete = models.CASCADE, default = None)

    def __str__(self):
        if self.item:
            return f"{self.item.nome}"
        else:
            return f"{self.livro.titulo}"
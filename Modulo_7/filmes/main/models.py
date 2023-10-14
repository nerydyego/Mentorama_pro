from django.db import models
from datetime import datetime as dt

class ProjetoFilmes(models.Model):
    # Aqui definimos as colunas que teremos em nosso banco de dados
    titulo = models.CharField(max_length=100)
    categoria = models.CharField(max_length=50)
    descricao = models.TextField()
    ano = models.IntegerField("Ano do Filme")
    data = models.DateTimeField("Cadastrado em", default=dt.now())

    def __str__(self):
        return self.titulo
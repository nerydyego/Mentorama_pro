from django.db import models
from datetime import datetime as dt

class ProjetoDjango(models.Model):
    # Aqui definimos as colunas que teremos em nosso banco de dados
    titulo = models.CharField(max_length=50)
    descricao = models.TextField()
    numero_de_modulos = models.DecimalField(max_digits=1000, decimal_places=2)
    data = models.DateTimeField("Publicado em", default=dt.now())

from datetime import datetime

from django.db import models


# Create your models here.
class Post(models.Model):
    autor = models.CharField(max_length =255)
    titulo = models.CharField(max_length =255)
    subtitulo = models.CharField(max_length =255)
    conteudo = models.TextField()
    data_publicacao = models.DateTimeField(default = datetime.now())
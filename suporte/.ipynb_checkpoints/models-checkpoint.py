from django.db import models

# Create your models here.
class Artigos(models.Model):
    titulo_text = models.CharField(max_length=200)
    descricao_text = models.CharField(max_length=200)
    artigos_date = models.DateTimeField('date published')


#class Chamados(models.Model):
 #   titulo_text = models.CharField(max_length=200)
  #  descricao_text = models.CharField(max_length=200)
   # prioridade_text = models.CharField(max_length=200)
    #departamento_text = models.CharField(max_length=200)
   # autor_text = models.CharField(max_length=200)
    #chamados_date = models.DateTimeField('date published')

from django.db import models
CRC_CHOICES = (
    ('CRC', 'CRC'),
    ('Registro Civil', 'Registro Civil'),
    ('CRC Jud', 'CRC Jud'),
)
# Create your models here.
class Artigos(models.Model):
    titulo_text = models.CharField(max_length=200)
    descricao_text = models.CharField(max_length=200)
    artigos_date = models.DateTimeField('date published')

class Ticket(models.Model):
    titulo_text = models.CharField(max_length=200)
    descricao_text = models.CharField(max_length=200)
    prioridade_text = models.CharField(max_length=200)
    departamento_text = models.CharField(max_length=200,choices=CRC_CHOICES)
    autor_text = models.CharField(max_length=200)
    chamados_date = models.DateTimeField('date published')

class Dialogo(models.Model):
    tipo_text = models.CharField(max_length=200)
    autor_text = models.CharField(max_length=200)
    conteudo_text = models.CharField(max_length=200)
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
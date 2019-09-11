from django.db import models
from django.urls import reverse
import uuid

CRC_CHOICES = (
    ('CRC', 'CRC'),
    ('Registro Civil', 'Registro Civil'),
    ('CRC Jud', 'CRC Jud'),
)
# Create your models here.

def generate_ticket_id():
    return str(uuid.uuid4()).split("-")[-1] #generate unique ticket id

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
    ticket_id = models.CharField(max_length=255, blank=True)
    ticket_email = models.CharField(max_length=255, blank=True)
    chamados_date = models.DateTimeField('date published')
    def get_absolute_url(self):
        return reverse('tickets_detail', kwargs={'pk': self.pk})
    def save(self, *args, **kwargs):
        self.ticket_id = generate_ticket_id()
        self.prioridade_text = "BAIXA"
        super(Ticket, self).save(*args, **kwargs) # Call the real   save() method

class Dialogo(models.Model):
    tipo_text = models.CharField(max_length=200)
    autor_text = models.CharField(max_length=200)
    conteudo_text = models.CharField(max_length=200)
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
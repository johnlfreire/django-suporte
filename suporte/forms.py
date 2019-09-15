from django import forms
from .models import Artigos, Ticket, CRC_CHOICES
import datetime

class LoginForm(forms.Form):
    
    username = forms.CharField(
         max_length=255,
         widget=forms.TextInput(attrs={'class': 'form-control'})
     )    
    password = forms.CharField(
         max_length=255,
         widget=forms.PasswordInput(attrs={'class': 'form-control'})
     )

class ArtigosForm(forms.Form):
        
    titulo = forms.CharField(
         max_length=255,
         widget=forms.TextInput(attrs={'class': 'form-control'})
     )    
    descricao = forms.CharField(
         max_length=255,
         widget=forms.Textarea(attrs={'class': 'form-control ','rows':'5'})
     )
class TicketSimpleForm(forms.Form):
        
    ticket_id = forms.CharField(
         max_length=255,
         widget=forms.TextInput(attrs={'class': 'form-control'})
     )    
    ticket_email = forms.CharField(
         max_length=255,
         widget=forms.TextInput(attrs={'class': 'form-control'})
     )    
class TicketForm(forms.ModelForm):
    titulo_text = forms.CharField(
         max_length=255,
         widget=forms.TextInput(attrs={'class': 'form-control'}), 
         label="Titulo"
         
     )    
    descricao_text = forms.CharField(
         max_length=255,
         widget=forms.Textarea(attrs={'class': 'form-control','rows':'5'}), 
         label="Descrição"
         
     )
    prioridade_text = forms.CharField(
         max_length=255,
         widget=forms.TextInput(attrs={'class': 'form-control'}),
         label="Prioridade"
     )    
    departamento_text = forms.ChoiceField(         
         choices = CRC_CHOICES,
         initial='',
         widget=forms.Select(attrs={'class': 'form-control'}), 
         label="Departamento"
     )
    autor_text = forms.CharField(
         max_length=255,
         widget=forms.TextInput(attrs={'class': 'form-control'}), 
         label="Autor"
     )
    chamados_date = forms.DateField(
        widget=forms.widgets.DateInput(format="%m/%d/%Y",attrs={'class': 'form-control'})
    )        
    ticket_id = forms.CharField(
         max_length=255,
         widget=forms.TextInput(attrs={'class': 'form-control','disabled':''}),
         required=False
    
     )
    ticket_email = forms.EmailField(
    widget=forms.EmailInput(attrs={'class': 'form-control'})
    ) 
    
    class Meta:
      model = Ticket
      fields = ('titulo_text','ticket_id','descricao_text','departamento_text','autor_text','ticket_email','chamados_date','prioridade_text')

class ResumTicketForm(forms.ModelForm):
    class Meta:
      model = Ticket      
      fields = ('titulo_text','descricao_text','autor_text','ticket_email','departamento_text','chamados_date')
      widgets = {
            'titulo_text':forms.TextInput(attrs={'class': 'form-control'}),
            'descricao_text':forms.Textarea(attrs={'class': 'form-control','rows':'5'}),
            'autor_text':forms.TextInput(attrs={'class': 'form-control'}),
            'ticket_email':forms.EmailInput(attrs={'class': 'form-control'}),
            'departamento_text':forms.Select(attrs={'class': 'form-control'}),
            'chamados_date':forms.HiddenInput(attrs={'class': 'form-control'})
        }
      labels = {
          'titulo_text':('Titulo'),
          'descricao_text':('Descrição'),
          'autor_text':('Nome'),
          'ticket_email':('Email'),
          'departamento_text':('Departamento'),
          'chamados_date':('Data'),
      }
        #help_texts = {
         #   'name': _('Some useful help text.'),
        #}
        #error_messages = {
         #   'name': {
          #      'max_length': _("This writer's name is too long."),
           # },
        #}
      #fields = '__all__'
    
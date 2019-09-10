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
         widget=forms.Textarea(attrs={'class': 'form-control','rows':'5'})
     )
class TicketSimpleForm(forms.Form):
        
    ticket_id = forms.CharField(
         max_length=255,
         widget=forms.TextInput(attrs={'class': 'form-control'})
     )    
    email = forms.CharField(
         max_length=255,
         widget=forms.Textarea(attrs={'class': 'form-control','rows':'5'})
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
    chamados_date = forms.CharField(
         max_length=255,
         widget=forms.HiddenInput(attrs={'class': 'form-control'}), 
         label="Data"
     )    
    class Meta:
      model = Ticket
      widgets = {'chamados_date': forms.HiddenInput()}
      fields = ('titulo_text','descricao_text','prioridade_text','departamento_text','autor_text','chamados_date')
    
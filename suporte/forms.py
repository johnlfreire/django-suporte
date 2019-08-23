from django import forms

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
from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, HttpResponseRedirect, HttpRequest
from .forms import LoginForm, ArtigosForm
from django.contrib.auth import authenticate, login as django_login
from django.contrib.auth.decorators import login_required
from .models import Artigos
from django.core.paginator import Paginator
from django.views.generic.edit import CreateView, UpdateView, DeleteView
import datetime

def login(request):
    form = LoginForm()
    if request.method == 'GET':
        return render(request, 'app/login.html',{'form':form})
    
    username = request.POST.get('username')
    password = request.POST.get('password')
    
    user = authenticate(username=username, password=password)
    
    if user:
        django_login(request, user)
        return redirect('/home/')
    
    message = 'Credenciais inválidas'
    return render(request, 'app/login.html',{'form':form,'message': message})


@login_required(login_url='/login')
def home(request):
    artigos_list = Artigos.objects.all()
    paginator = Paginator(artigos_list, 3) 
    form = ArtigosForm()
    page = request.GET.get('page')
    artigos = paginator.get_page(page)
    return render(request, 'app/home.html',{'artigos':artigos,'form':form})


#@login_required(login_url='/login')
#def home(request):
#@login_required(login_url='/login')
#class NotesCreateView(CreateView):
#    template_name = 'app/home.html'
#    model = Artigos
#    fields = ['titulo_text', 'descricao_text']
#    sucess_url = ''
    
def notes(request):  
    if request.method == 'GET':
        return redirect('')
    else:
        form = ArtigosForm(request.POST)
        if form.is_valid():
            Artigos.objects.create(
                titulo_text=form.cleaned_data['titulo'],
                descricao_text=form.cleaned_data['descricao'],
                artigos_date = datetime.datetime.now()
            )
            return redirect('/')
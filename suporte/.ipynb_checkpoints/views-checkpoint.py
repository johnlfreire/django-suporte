from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, HttpResponseRedirect, HttpRequest
from .forms import LoginForm
from django.contrib.auth import authenticate, login as django_login
from django.contrib.auth.decorators import login_required
from .models import Artigos
from django.core.paginator import Paginator
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

    page = request.GET.get('page')
    artigos = paginator.get_page(page)
    return render(request, 'app/home.html',{'artigos':artigos})
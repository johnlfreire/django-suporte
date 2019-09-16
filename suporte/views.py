from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, HttpResponseRedirect, HttpRequest
<<<<<<< HEAD
from .forms import LoginForm, ArtigosForm, TicketForm,TicketSimpleForm,ResumTicketForm
=======
from .forms import LoginForm, ArtigosForm, TicketForm,TicketSimpleForm
>>>>>>> 7b39512b683580ce09ea79cfa53c7606dd3a81ec
from django.core.paginator import Paginator
from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from django.contrib.auth.decorators import login_required
from .models import Artigos, Ticket,Dialogo
from django.views.generic import ListView, DetailView,CreateView
from django.views.generic.edit import  UpdateView, DeleteView,FormView
from django.urls import reverse_lazy
import datetime
from django.utils.translation import gettext_lazy as _
def login(request):
    form = LoginForm()
    if request.method == 'GET':
        return render(request, 'suporte/login.html',{'form':form})    
    username = request.POST.get('username')
    password = request.POST.get('password')    
    user = authenticate(username=username, password=password)    
    if user:
        django_login(request, user)
        return redirect('/home/')    
    message = 'Credenciais inválidas'
    return render(request, 'suporte/login.html',{'form':form,'message': message})

@login_required(login_url='/login')
def home(request):
    artigos_list = Artigos.objects.all()
    paginator = Paginator(artigos_list, 3) 
    form = ArtigosForm()
    page = request.GET.get('page')
    artigos = paginator.get_page(page)
    return render(request, 'suporte/home.html',{'artigos':artigos,'form':form})


#@login_required(login_url='/login')
#def home(request):
#@login_required(login_url='/login')
#class NotesCreateView(CreateView):
#    template_name = 'suporte/home.html'
#    model = Artigos
#    fields = ['titulo_text', 'descricao_text']
#    sucess_url = ''
def teste(request):
    print(request.POST['area2']) 
    print(request.POST['file']) 
    return redirect('/home/')     
         

def notes(request):  
    if request.method == 'GET':
        return redirect('/home/')
    else:
        form = ArtigosForm(request.POST)
        if form.is_valid():
            Artigos.objects.create(
                titulo_text=form.cleaned_data['titulo'],
                descricao_text=form.cleaned_data['descricao'],
                artigos_date = datetime.datetime.now()
            )
            return redirect('/home/')

@login_required(login_url='/login')
def logout(request):
    django_logout(request)
    return redirect('/login/')  

class TicketCreate(CreateView): 
    
    #chamados_date = datetime.datetime.now()
    form_class = ResumTicketForm 
    initial = {'chamados_date': datetime.datetime.now()}
    
    template_name = 'suporte/ticket/tickets_create.html'
    
    #success_url = '/tickets'
    #fields = '__all__'
    #model = Ticket    
    
    
    
    #fields = ('titulo_text','descricao_text','prioridade_text','departamento_text','autor_text','chamados_date')
    #form_class = TicketForm    
   # chamados_date = datetime.datetime.now()
    #def form_valid(self, form):
     #   new_item = form.save(commit=False)
      #  return super().form_valid(form)
    

    
def ticketForm(request):
     #if request.method == 'POST':
    #try:
     #   ar = Ticket.objects.filter(ticket_id='ac6205329a9c').filter(pk=24)
       
    #except Ticket.DoesNotExist:
     #   print('ERROOO')
    form = TicketSimpleForm()
    return render(request, 'suporte/ticket/tickets_user_form.html',{'form':form})  

def TicketQuery(request):
     #if request.method == 'POST':
    try:
        ar = Ticket.objects.filter(ticket_id='ac6205329a9c').filter(pk=24)
        print(ar)  
    except Ticket.DoesNotExist:
        print('ERROOO')
    return redirect('/home/')
class TicketList(ListView): 
    template_name = 'suporte/ticket/tickets_list.html'
    model = Ticket
    form_class = TicketForm 
class TicketDetail(DetailView): 
    artigos = Artigos.objects.all()
    #template_name =('suporte/ticket/tickets_detail.html',{'artigos'artigos})
    template_name = 'suporte/ticket/tickets_detail.html'
    model = Ticket    
    form_class = TicketForm
    def get_context_data(self, **kwargs):
        context = super(TicketDetail, self).get_context_data(**kwargs)
        context['dialogo'] = Dialogo.objects.filter(ticket_id=32)
        return context

class TicketUpdate(UpdateView): 
    template_name = 'suporte/ticket/tickets_form.html'
    model = Ticket 
    form_class = TicketForm
    print()    
    #chamados_date = datetime.datetime.now()
    success_url = reverse_lazy('tickets_list')


class TicketDelete(DeleteView):
    template_name = 'suporte/ticket/tickets_confirm_delete.html'
    model = Ticket
    success_url = reverse_lazy('tickets_list')                  
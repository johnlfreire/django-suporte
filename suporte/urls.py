from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('login/', views.login),    
    path('notes/', views.notes),
    path('teste/', views.teste),
    path('logout/', views.logout),
    path('query/', views.TicketQuery),
    path('form/', views.ticketForm),    
    path('tickets/create/', views.TicketCreate.as_view(), name='tickets_create'),
    path('tickets/', views.TicketList.as_view(), name='tickets_list'),
    path('tickets/<int:pk>', views.TicketDetail.as_view(), name='tickets_detail'),
    path('tickets/update/<int:pk>', views.TicketUpdate.as_view(), name='tickets_update'),
    path('tickets/delete/<int:pk>', views.TicketDelete.as_view(), name='tickets_delete'),
]
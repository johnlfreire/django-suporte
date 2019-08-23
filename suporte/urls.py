from django.urls import path
#from suporte.views import NotesCreateView
from . import views

urlpatterns = [
    path('login/', views.login),
    path('', views.home),
    #path('notes/', NotesCreateView.as_view()),
    path('notes/', views.notes),
]
from django.shortcuts import render

# Create your views here.
# core/views.py
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView
from .models import Setor, Interessado

# Views para Setor
class HomeView(TemplateView):
     model = Setor
     context_object_name = 'setores'
     template_name = 'core/home.html'

class SetorListView(ListView):
    model = Setor
    template_name = 'core/setor_list.html'
    context_object_name = 'setores'

class SetorCreateView(CreateView):
    model = Setor
    fields = ['nome', 'descricao']
    template_name = 'core/setor_form.html'
    success_url = reverse_lazy('setor-list')

class SetorUpdateView(UpdateView):
    model = Setor
    fields = ['nome', 'descricao']
    template_name = 'core/setor_form.html'
    success_url = reverse_lazy('setor-list')

class SetorDeleteView(DeleteView):
    model = Setor
    template_name = 'core/setor_confirm_delete.html'
    success_url = reverse_lazy('setor-list')

# Views para Interessado
class InteressadoListView(ListView):
    model = Interessado
    context_object_name = 'interessados'
    template_name = 'core/interessado_list.html'

class InteressadoCreateView(CreateView):
    model = Interessado
    fields = ['nome', 'setor']
    template_name = 'core/interessado_form.html'
    success_url = reverse_lazy('interessado-list')

class InteressadoUpdateView(UpdateView):
    model = Interessado
    fields = ['nome', 'setor']
    template_name = 'core/interessado_form.html'
    success_url = reverse_lazy('interessado-list')

class InteressadoDeleteView(DeleteView):
    model = Interessado
    template_name = 'core/interessado_confirm_delete.html'
    success_url = reverse_lazy('interessado-list')
    
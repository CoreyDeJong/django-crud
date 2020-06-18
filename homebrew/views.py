from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Beers
from django.urls import reverse_lazy

# Create your views here.

class HomeView(TemplateView):
    template_name = 'base.html'

class BeerListView(ListView):
    template_name = 'beer_list.html'
    model = Beers

class BeerDetailView(DetailView):
    template_name = 'beer_detail.html'
    model = Beers

class BeerCreateView(CreateView):
    template_name = 'beer_create.html'
    model = Beers
    fields = ['brewery', 'name', 'abv', 'ibu', 'description']

class BeerUpdateView(UpdateView):
    template_name = 'beer_update.html'
    model = Beers
    fields = ['brewery', 'name', 'abv', 'ibu', 'description']

class BeerDeleteView(DeleteView):
    template_name = 'beer_delete.html'
    model = Beers
    success_url = reverse_lazy('beer_list')
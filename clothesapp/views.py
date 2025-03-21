from django.shortcuts import render
from django.views.generic import ListView,DetailView
from clothesapp import models


class Main(ListView):
    model = models.Clothes
    template_name = 'main.html'
    context_object_name = 'items'


class ClothesView(DetailView):
    model = models.Clothes
    template_name = 'detail.html'
    context_object_name = 'items'


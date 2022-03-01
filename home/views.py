from django.shortcuts import render
from django.views import generic


class HomeView(generic.ListView):
    queryset = ''
    template_name = 'index.html'

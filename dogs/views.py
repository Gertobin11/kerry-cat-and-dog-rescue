from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from .models import DogAdoption
from .forms import DogAdoptionForm


class DogAdoptionView(SuccessMessageMixin, CreateView):
    """ View to handle creating a new blog post """
    model = DogAdoption
    form_class = DogAdoptionForm
    success_url = '/blog/'
    template_name = 'dog-adoption.html'
    success_message = ('Your Application made through %(email)s was'
                       ' uploaded successfully')

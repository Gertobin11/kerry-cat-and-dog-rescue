from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from blog.models import Post
from .models import CatAdoptionModel
from .forms import CatAdoptionForm


class CatAdoption(ListView):
    """ A view to display all posts related to cats """
    model = Post
    queryset = Post.objects.filter(category=1).order_by('created_on')
    paginate_by = 6
    template_name = 'cat-list.html'


class CatAdoptionQuestionaire(SuccessMessageMixin, CreateView):
    """ A view to display the the cat adoption form """
    model = CatAdoptionModel
    form_class = CatAdoptionForm
    success_url = '/blog/'
    template_name = 'dog-adoption.html'
    success_message = ('Your Application made through %(email)s was'
                       ' uploaded successfully')


def tnr(request):
    """ Function to render the TNR page """
    template = "tnr.html"
    return render(request, template)

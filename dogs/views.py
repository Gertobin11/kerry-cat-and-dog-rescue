from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from blog.models import Post
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


class DogView(generic.ListView):
    """ A view to display al the posts associated with dogs """
    model = Post
    queryset = Post.objects.filter(category=2).order_by('-created_on')
    paginate_by = 6
    template_name = 'dog-list.html'
    

def dog_neuter_info(request):
    """ Function to display information about neutering """
    template = 'dog-neuter.html'

    return render(request, template)

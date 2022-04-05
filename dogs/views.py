from django.shortcuts import render
from django.views import generic, View
from django.views.generic.edit import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import PermissionRequiredMixin
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


class DisplaySubmittedForms(PermissionRequiredMixin, generic.ListView):
    """ Class to display all the completed user forms """
    permission_required = "dogadoption.change_dogadoption"
    model = DogAdoption
    queryset = DogAdoption.objects.all()
    paginate_by = 6
    template_name = 'dog-completed-forms.html'


class FormDetailView(PermissionRequiredMixin, View):
    """ Class to handle displaying the applications made """
    permission_required = "dogadoption.change_dogadoption"

    def get(self, request, post_id, *args, **kwargs):
        """ View to display an individual appication """
        queryset = DogAdoption.objects.all().order_by('-applied_on')
        application = get_object_or_404(queryset, id=post_id)
        context = {
            'application': application
        }
        template = 'dog-form-details.html'
        return render(request, template, context)


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

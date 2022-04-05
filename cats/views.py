from django.shortcuts import render
from django.views.generic import ListView, View
from django.views.generic.edit import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import get_object_or_404
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


class DisplaySubmittedCatForms(PermissionRequiredMixin, ListView):
    """ Class to display all the completed user forms """
    permission_required = "catadoptionmodel.change_catadoptionmodel"
    model = CatAdoptionModel
    queryset = CatAdoptionModel.objects.all().order_by('-applied_on')
    paginate_by = 6
    template_name = 'cat_completed_forms.html'


class CatFormDetailView(PermissionRequiredMixin, View):
    """ Class to handle displaying the applications made """
    permission_required = "catadoptionmodel.change_catadoptionmodel"

    def get(self, request, post_id, *args, **kwargs):
        """ View to display an individual appication """
        queryset = CatAdoptionModel.objects.all()
        application = get_object_or_404(queryset, id=post_id)
        context = {
            'application': application
        }
        template = 'cat_form_details.html'
        return render(request, template, context)

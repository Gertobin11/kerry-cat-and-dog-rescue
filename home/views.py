from django.shortcuts import render
from django.shortcuts import get_list_or_404
from django.views import generic
from blog.models import Post


class HomeView(generic.ListView):
    model = Post()
    queryset = Post.objects.all().order_by('-created_on')[:5]
    template_name = 'index.html'

from django.urls import path
from . import views


urlpatterns = [
    path('cat-adoption', views.CatAdoption.as_view(), name='cat-adoption'),
    path('cat-adoption-questionaire', views.CatAdoptionQuestionaire.as_view(),
         name='cat-adoption-questionaire'),
    path('tnr', views.tnr, name='tnr')
]

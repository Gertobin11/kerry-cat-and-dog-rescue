from django.urls import path
from . import views


urlpatterns = [
    path('cat-adoption', views.CatAdoption.as_view(), name='cat-adoption'),
    path('cat-adoption-questionaire', views.CatAdoptionQuestionaire.as_view(),
         name='cat-adoption-questionaire'),
    path('tnr', views.tnr, name='tnr'),
    path('cat-forms', views.DisplaySubmittedCatForms.as_view(),
         name='cat_forms'),
    path('cat-form/<int:post_id>', views.CatFormDetailView.as_view(),
         name='cat_form_details')
]

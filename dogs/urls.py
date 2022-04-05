from django.urls import path
from . import views


urlpatterns = [
    path("dog-adoption", views.DogAdoptionView.as_view(), name="dog-adoption"),
    path("dog-list", views.DogView.as_view(), name="dog-list"),
    path("dog-neuter", views.dog_neuter_info, name="dog-neuter"),
    path("dog-forms", views.DisplaySubmittedForms.as_view(), name='dog-forms'),
    path("dog_form_details/<int:post_id>", views.FormDetailView.as_view(),
         name='dog_form_details')
]

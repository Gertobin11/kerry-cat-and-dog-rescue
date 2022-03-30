from django.urls import path
from . import views


urlpatterns = [
    path("dog-adoption", views.DogAdoptionView.as_view(), name="dog-adoption"),
    path("dog-list", views.DogView.as_view(), name="dog-list"),
    path("dog-neuter", views.dog_neuter_info, name="dog-neuter")
]

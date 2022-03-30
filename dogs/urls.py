from django.urls import path
from . import views


urlpatterns = [
    path("dog-adoption", views.DogAdoptionView.as_view(), name="dog-adoption")
]
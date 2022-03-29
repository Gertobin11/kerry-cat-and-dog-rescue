from django.contrib import admin
from . models import DogAdoption

@admin.register(DogAdoption)
class DogAdoptionAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'eircode')
    search_fields = ['name']

from django.contrib import admin
from .models import CatAdoptionModel


@admin.register(CatAdoptionModel)
class CatAdoptionAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'eircode')
    search_fields = ['name']


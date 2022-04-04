from django import forms
from .models import CatAdoptionModel


class CatAdoptionForm(forms.ModelForm):
    """ Handles what will display in the form """
    class Meta:
        """ Specify the details of what to display """
        model = CatAdoptionModel

        fields = ('name', 'email', 'phone', 'county', 'address',
                  'eircode', 'homeowner', 'other_cats', 'neutered',
                  'other_animals')

        labels = {
            "name": "Please enter your full name",
            "email": "Email Address",
            "phone": "Phone Number",
            "county": "Please Select Your County",
            "address": "Please Enter your Address",
            "eircode": "Please Enter A valid Eircode",
            "homeowner": "Are you the homeowner?",
            "other_cats": "Do you have other cats at the home?",
            "neutered": "If yes, Are they neutered?",
            "other_animals": "Do you have other animals at the home? If yes please identify them"
        }

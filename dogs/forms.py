from django import forms
from .models import DogAdoption


class DogAdoptionForm(forms.ModelForm):
    """ Form for users to fill out to add their
     data to the dg adoption database """
    class Meta:
        """ Details of what to be displayed in the form """
        model = DogAdoption
        fields = ('name', 'email', 'phone', 'county', 'address', 'eircode',
                  'reason_for_dog', 'dog_hours_alone', 'indoor_outdoor',
                  'size_of_dog', 'specific_dog', 'name_breed', 'age_of_dog',
                  'people_living_address',
                  'people_age', 'allergies', 'children_at_address',
                  'childrens_ages', 'accomodation_type',
                  'homeowner', 'garden_type', 'other_dogs', 'neutered',
                  'other_animals')

        labels = {
            "name": "Please enter your full name",
            "email": "Email Address",
            "phone": "Phone Number",
            "county": "Please Select Your County",
            "address": "Please Enter your Address",
            "eircode": "Please Enter A valid Eircode",
            "reason_for_dog": "Why are you looking to adopt a dog",
            "dog_hours_alone": "Please select how may hours the dog is likely to spend alone each day",
            "indoor_outdoor": "Please state your preference for an indoor or outdoor dog",
            "size_of_dog": "Please select which size dog would best suite your needs",
            "specific_dog": "Please select if you looking for a specific breed of dog",
            "name_breed": "If yes , then which breed are you looking for?",
            "age_of_dog": "What age of a dog would best suite you?",
            "people_living_address": "How many people are living in your home?",
            "people_age": "Please seect which age bracket best describes the people living in your home",
            "allergies": "Does anyone in the home suffer from allergies i.e. asthma?",
            "children_at_address": "Are there Children living in the home?",
            "childrens_ages": "If yes, then what are the childrens ages?",
            "accomodation_type": "Please select what option best describes your home",
            "homeowner": "Are you the homeowner?",
            "garden_type": "Please describe the layout of your garden i.e. fenced, grass",
            "other_dogs": "Do you have other dogs at the home?",
            "neutered": "If yes, Are they neutered?",
            "other_animals": "Do you have other animals at the home? If yes please identify them"
        }

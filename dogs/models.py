from django.db import models
from django.contrib.auth.models import User


COUNTIES = (('Antrim', 'Antrim'), ('Armagh', 'Armagh'), ('Carlow', 'Carlow'),
            ('Cavan', 'Cavan'), ('Clare', 'Clare'), ('Cork', 'Cork'),
            ('Derry', 'Derry'), ('Donegal', 'Donegal'), ('Down', 'Down'),
            ('Dublin', 'Dublin'), ('Fermanagh', 'Fermanagh'),
            ('Galway', 'Galway'),
            ('Kerry', 'Kerry'), ('Kildare', 'Kildare'),
            ('Kilkenny', 'Kilkenny'),
            ('Laois', 'Laois'), ('Leitrim', 'Leitrim'),
            ('Limerick', 'Limerick'),
            ('Longford', 'Longford'), ('Louth', 'Louth'), ('Mayo', 'Mayo'),
            ('Meath', 'Meath'), ('Monaghan', 'Monaghan'), ('Offaly', 'Offaly'),
            ('Roscommon', 'Roscommon'), ('Sligo', 'Sligo'),
            ('Tipperary', 'Tipperary'),
            ('Tyrone', 'Tyrone'), ('Waterford', 'Waterford'),
            ('Westmeath', 'Westmeath'),
            ('Wexford', 'Wexford'), ('Wicklow', 'Wicklow'))

YES_NO = (('Yes', 'Yes'), ('No', 'No'))

INDOOR_OUTDOOR = (("Don't Mind", "Don't Mind"), ("Indoor", "Indoor"),
                  ("Outdoor", "Outdoor"))

DOG_SIZES = (("Don't Mind", "Don't Mind"), ("Tiny", "Tiny"),
             ("Small", "Small"), ("Medium", "Medium"),
             ("Large", "Large"))

DOG_AGE = (("Don't Mind", "Don't Mind"), ("< 12 months", "< 12 months"),
           ("1 - 4 Years", "1 - 4 Years"), ("5 - 8 Years", "5 - 8 Years"),
           ("Senior", "Senior"))

AGES = (("18-40", "18-40"), ("41-60", "41-60"), ("61+", "61+"))

ACCOMODATION = (('House', 'House'), ('Townhouse', 'Townhouse'),
                ('Apartment', 'Apartment'), ('Other', 'Other'))


class DogAdoption(models.Model):
    """ Model for storing adoption questionaire info """
    name = models.CharField(blank=False, null=False, max_length=200)
    email = models.EmailField(blank=False, null=False)
    phone = models.IntegerField(blank=False, null=False)
    county = models.CharField(blank=False, null=False,
                              choices=COUNTIES, max_length=240)
    address = models.TextField(blank=False, null=False)
    eircode = models.CharField(blank=False, null=False, max_length=240)
    reason_for_dog = models.TextField(blank=False, null=False)
    dog_hours_alone = models.IntegerField(blank=False, null=False)
    indoor_outdoor = models.CharField(blank=False, null=False, max_length=240,
                                      choices=INDOOR_OUTDOOR)
    size_of_dog = models.CharField(blank=False, null=False, choices=DOG_SIZES,
                                   max_length=240)
    specific_dog = models.CharField(blank=False, null=False, choices=YES_NO,
                                    max_length=240)
    name_breed = models.CharField(blank=True, null=True, max_length=240)
    age_of_dog = models.CharField(blank=False, null=False, choices=DOG_AGE,
                                  max_length=240)
    people_living_address = models.SmallIntegerField(blank=False, null=False)
    people_age = models.CharField(blank=False, null=False, choices=AGES,
                                  max_length=240)
    allergies = models.CharField(blank=False, null=False, choices=YES_NO,
                                 max_length=240)
    children_at_address = models.CharField(blank=False, null=False,
                                           choices=YES_NO, max_length=240)
    childrens_ages = models.CharField(blank=True, null=True, max_length=240)
    accomodation_type = models.CharField(blank=False,
                                         null=False, choices=ACCOMODATION,
                                         max_length=240)
    homeowner = models.CharField(blank=False, null=False,
                                 choices=YES_NO, max_length=240)
    garden_type = models.TextField(blank=False, null=False)
    other_dogs = models.CharField(blank=False, null=False, choices=YES_NO,
                                  max_length=240)
    neutered = models.CharField(blank=True, null=True, choices=YES_NO,
                                max_length=240)
    other_animals = models.TextField(blank=False, null=False)
    applied_on = models.DateTimeField(blank=False, null=False,
                                      auto_now_add=True)

    def __str__(self):
        return self.name






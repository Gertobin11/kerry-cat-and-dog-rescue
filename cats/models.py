from django.db import models
from dogs.models import COUNTIES, YES_NO


class CatAdoptionModel(models.Model):
    """ Model to hold data for people looking to adopt a cat """
    name = models.CharField(blank=False, null=False, max_length=200)
    email = models.EmailField(blank=False, null=False)
    phone = models.IntegerField(blank=False, null=False)
    county = models.CharField(blank=False, null=False,
                              choices=COUNTIES, max_length=240)
    address = models.TextField(blank=False, null=False)
    eircode = models.CharField(blank=False, null=False, max_length=240)
    homeowner = models.CharField(blank=False, null=False,
                                 choices=YES_NO, max_length=240)
    other_cats = models.CharField(blank=False, null=False, choices=YES_NO,
                                  max_length=240)
    neutered = models.CharField(blank=True, null=True, choices=YES_NO,
                                max_length=240)
    other_animals = models.TextField(blank=False, null=False)
    applied_on = models.DateTimeField(blank=False, null=False,
                                      auto_now_add=True)

    def __str__(self):
        """ Return the name of the Applicant"""
        return self.name

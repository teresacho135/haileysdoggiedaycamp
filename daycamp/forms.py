from django import forms
from .models import Camper, Schedule, Payment

class CamperForm(forms.ModelForm):
  class Meta:
    model = Camper
    fields = ('pet_name', 'age', 'isActive', 'food_amount', 'medicine', 'owner')


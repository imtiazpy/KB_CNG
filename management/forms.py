from django import forms

from .models import Fuel



class SaveFuelForm(forms.ModelForm):

  class Meta:
    model = Fuel
    fields = ('name', 'description', 'price', 'status')
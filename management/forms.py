from django import forms

from .models import Fuel, Stock



class SaveFuelForm(forms.ModelForm):

  class Meta:
    model = Fuel
    fields = ('name', 'description', 'price', 'status')

  def clean_name(self):
    name = self.cleaned_data['name']
    id = self.data['id'] if self.data['id'].isdigit() else 0

    if Fuel.objects.filter(name=name).exclude(id=id).exists():
      raise forms.ValidationError(f"{name} already exists.")

    return name



class SaveStockForm(forms.ModelForm):

  class Meta:
    model = Stock
    fields = ('fuel', 'volume', 'date')
  
  def clean_fuel(self):
    fuel_id = self.data.get('fuel')
    try:
      fuel = Fuel.objects.get(id=fuel_id)
      return fuel
    except Fuel.DoesNotExist:
      raise forms.ValidationError(f"Fuel with ID {fuel_id} does not exist.")
    except ValueError:
      raise forms.ValidationError("Invalid Fuel ID.")

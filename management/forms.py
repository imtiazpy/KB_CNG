from django import forms

from .models import Fuel, Stock, Sale



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
  
  def clean_price(self):
    price = self.cleaned_data['price']
    
    if price > 0:
      return price
    raise forms.ValidationError("Invalid price. Please enter a value greater than 0")



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
  
  def clean_volume(self):
    volume = self.cleaned_data['volume']
    if volume > 0:
      return volume
    raise forms.ValidationError("Invalid volume. Please enter a value greater than 0")
  
class SaveSaleForm(forms.ModelForm):
  class Meta:
    model = Sale
    fields = ('fuel', 'volume', 'date', 'customer_name', 'price', 'total_amount')
  
  def clean_fuel(self):
    fuel_id = self.data.get('fuel')
    try:
      fuel = Fuel.objects.get(id=fuel_id)
      return fuel
    except Fuel.DoesNotExist:
      raise forms.ValidationError(f"Fuel with ID {fuel_id} does not exist.")
    except ValueError:
      raise forms.ValidationError("Invalid Fuel ID.")
    
  def clean_volume(self):
    fuel_vol = Fuel.objects.get(id=self.data.get('fuel')).available()
    volume = self.data.get('volume')

    if float(volume) <= 0:
      raise forms.ValidationError("Volume must be greater than 0.")
    elif float(volume) <= float(fuel_vol):
      return volume
    else: 
      raise forms.ValidationError(f"Fuel volume exceeds the limit. Available fuel - {fuel_vol} L")
    
  def clean_price(self):
    fuel_id = self.data.get('fuel')
    fuel_price = Fuel.objects.get(id=fuel_id).price

    price = self.cleaned_data['price']

    if float(price) == float(fuel_price):
      return price
    raise forms.ValidationError(f"Invalid price! Please enter  a valid price.")
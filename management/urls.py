from django.urls import path
from .views import Dashboard, fuel_list_view, manage_fuel_view, add_fuel_view

urlpatterns = [
  path('', Dashboard.as_view(), name='dashboard'),
  path('fuel-list/', fuel_list_view, name='fuel_list'),
  path('manage-fuel/', manage_fuel_view, name='manage_fuel'),
  path('add-fuel/', add_fuel_view, name='add_fuel')

]
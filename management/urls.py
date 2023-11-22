from django.urls import path
from .views import Dashboard, fuel_list_view, manage_fuel_view, save_fuel_view, fuel_detail_view, fuel_delete_view

urlpatterns = [
  path('', Dashboard.as_view(), name='dashboard'),
  path('fuel-list/', fuel_list_view, name='fuel_list'),
  path('manage-fuel/', manage_fuel_view, name='manage_fuel'),
  path('manage-fuel-edit/<int:pk>/', manage_fuel_view, name='manage_fuel_edit'),
  path('add-fuel/', save_fuel_view, name='save_fuel'),
  path('fuel-detail/<int:pk>/', fuel_detail_view, name='fuel_detail'),
  path('delete-fuel/<int:pk>/', fuel_delete_view, name='delete_fuel'),
]
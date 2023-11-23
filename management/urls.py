from django.urls import path
from .views import Dashboard, fuel_list_view, manage_fuel_view, save_fuel_view, fuel_detail_view, fuel_delete_view, stock_list_view, manage_stock_view, save_stock_view, stock_detail_view, stock_delete_view, inventory_view

urlpatterns = [
  path('', Dashboard.as_view(), name='dashboard'),

  path('fuels/', fuel_list_view, name='fuel_list'),
  path('fuels/manage/', manage_fuel_view, name='manage_fuel'),
  path('fuels/manage/<int:pk>/', manage_fuel_view, name='manage_fuel_edit'),
  path('fuels/add/', save_fuel_view, name='save_fuel'),
  path('fuels/detail/<int:pk>/', fuel_detail_view, name='fuel_detail'),
  path('fuels/delete/<int:pk>/', fuel_delete_view, name='delete_fuel'),

  path('stocks/', stock_list_view, name='stock_list'),
  path('stocks/manage/', manage_stock_view, name='manage_stock'),
  path('stocks/manage/<int:pk>/', manage_stock_view, name='manage_stock_edit'),
  path('stocks/add/', save_stock_view, name='save_stock'),
  path('stocks/detail/<int:pk>/', stock_detail_view, name='stock_detail'),
  path('stocks/delete/<int:pk>/', stock_delete_view, name='delete_stock'),

  path('inventory/', inventory_view, name='inventory'),
]
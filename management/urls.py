from django.urls import path
from .views import Dashboard, fuel_list_view, manage_fuel_view, save_fuel_view, fuel_detail_view, fuel_delete_view, stock_list_view, manage_stock_view, save_stock_view, stock_detail_view, stock_delete_view

urlpatterns = [
  path('', Dashboard.as_view(), name='dashboard'),
  path('fuel-list/', fuel_list_view, name='fuel_list'),
  path('manage-fuel/', manage_fuel_view, name='manage_fuel'),
  path('manage-fuel-edit/<int:pk>/', manage_fuel_view, name='manage_fuel_edit'),
  path('add-fuel/', save_fuel_view, name='save_fuel'),
  path('fuel-detail/<int:pk>/', fuel_detail_view, name='fuel_detail'),
  path('delete-fuel/<int:pk>/', fuel_delete_view, name='delete_fuel'),
  path('stock-list/', stock_list_view, name='stock_list'),
  path('manage-stock/', manage_stock_view, name='manage_stock'),
  path('manage-stock-edit/<int:pk>/', manage_stock_view, name='manage_stock_edit'),
  path('add-stock/', save_stock_view, name='save_stock'),
  path('stock-detail/<int:pk>/', stock_detail_view, name='stock_detail'),
  path('delete-stock/<int:pk>/', stock_delete_view, name='delete_stock'),
]
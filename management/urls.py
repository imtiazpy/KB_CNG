from django.urls import path
from . import views

urlpatterns = [
  path('', views.Dashboard.as_view(), name='dashboard'),

  path('fuels/', views.fuel_list_view, name='fuel_list'),
  path('fuels/manage/', views.manage_fuel_view, name='manage_fuel'),
  path('fuels/manage/<int:pk>/', views.manage_fuel_view, name='manage_fuel_edit'),
  path('fuels/add/', views.save_fuel_view, name='save_fuel'),
  path('fuels/detail/<int:pk>/', views.fuel_detail_view, name='fuel_detail'),
  path('fuels/delete/<int:pk>/', views.fuel_delete_view, name='delete_fuel'),

  path('stocks/', views.stock_list_view, name='stock_list'),
  path('stocks/manage/', views.manage_stock_view, name='manage_stock'),
  path('stocks/manage/<int:pk>/', views.manage_stock_view, name='manage_stock_edit'),
  path('stocks/add/', views.save_stock_view, name='save_stock'),
  path('stocks/detail/<int:pk>/', views.stock_detail_view, name='stock_detail'),
  path('stocks/delete/<int:pk>/', views.stock_delete_view, name='delete_stock'),

  path('inventory/', views.inventory_view, name='inventory'),

  path('sales/', views.sales_list_view, name='sales'),
  path('sales/manage/', views.sales_manage_view, name='manage_sale'),
  path('sales/manage/<int:pk>/', views.sales_manage_view, name='manage_sale_edit'),
  path('sales/add/', views.sales_save_view, name='save_sale'),
  path('sales/detail/<int:pk>/', views.sales_detail_view, name='sale_detail'),
  path('sales/delete/<int:pk>/', views.sales_delete_view, name='delete_sale'),

  path('sales/report/', views.sales_report_view, name='sales_report_page'),
  path('sales/report/<str:report_date>/', views.sales_report_view, name='sales_report')
]
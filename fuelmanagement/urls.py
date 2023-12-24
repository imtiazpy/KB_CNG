from django.urls import path

from . import views

urlpatterns = [
  path('', views.Dashboard.as_view(), name='fuel_dashboard'),
  path('fuels/', views.FuelListView.as_view(), name='fuel_list'),
  path('fuels/detail/<int:pk>/', views.FuelDetailView.as_view(), name='fuel_detail'),
  path('fuels/manage/', views.FuelCreateUpdateView.as_view(), name='manage_fuel'),
  path('fuels/manage/<int:pk>/', views.FuelCreateUpdateView.as_view(), name='manage_fuel_edit'),
  path('fuels/save/', views.FuelCreateUpdateView.as_view(), name='save_fuel'),
  path('fuels/delete/<int:pk>/', views.FuelDeleteView.as_view(), name='delete_fuel'),
]
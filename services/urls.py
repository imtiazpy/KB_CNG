from django.urls import path
from .views import services_list_page, service_detail_page

urlpatterns = [
  path('', services_list_page, name='services'),
  path('service/<int:pk>/', service_detail_page, name='service_detail')
]
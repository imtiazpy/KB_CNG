from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from django.views import generic
from django.db.models import Sum
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
import json

from .models import Fuel
from .forms import SaveFuelForm

class Dashboard(LoginRequiredMixin, generic.View):

  def get(self, request, *args, **kwargs):
    
    total_fuel_count = Fuel.objects.filter(status = 1).count()
    fuels = Fuel.objects.filter(status=1)

    try:
      total_sale = Fuel.sales.aggregate(Sum('amount'))['amount_sum']
      if total_sale is None:
        total_sale = 0
    except:
      total_sale = 0

    context = {
      'total_fuel_count': total_fuel_count,
      'fuels': fuels,
      'total_sale': total_sale,
    }

    return render(request, 'management/dashboard.html', context)
  

@login_required
def fuel_list_view(request):
  fuels = Fuel.objects.all()

  return render(request, 'management/fuel_list.html', {'fuels': fuels})

@login_required
def manage_fuel_view(request, pk=None):
  context = {}
  if pk is not None:
    context['fuel'] = Fuel.objects.get(id=pk)
  return render(request, 'management/manage_fuel.html', context)

@login_required
def fuel_detail_view(request, pk=None):
  context = {}
  if pk is not None:
    fuel = Fuel.objects.get(id=pk)
    context['fuel'] = fuel
  return render(request, 'management/fuel_detail.html', context)

@login_required
def save_fuel_view(request):
  res = {'status': 'failed', 'msg': ''}
  if not request.method == 'POST':
    res['msg'] = 'No Data was sent'

  else:
    post = request.POST
    if post['id'] != '':
      fuel = Fuel.objects.get(id = post['id'])
      form = SaveFuelForm(request.POST, instance=fuel)
    else:
      form = SaveFuelForm(request.POST)

    if form.is_valid():
      form.save()
      if post['id'] == '':
        messages.success(request, "Fuel has been added successfully")
      else:
        messages.success(request, "Fuel has been updated successfully")

      res['status'] = 'success'
    else:
      for field in form:
          for error in field.errors:
            if not res['msg'] == '':
                res['msg'] += str('<br />')
            res['msg'] += str(f"[{field.label}] {error}")
  return HttpResponse(json.dumps(res), content_type="application/json")

@login_required
def fuel_delete_view(request, pk=None):
  res = {'status': '', 'msg': ''}

  if pk is None:
    res['msg'] = "Invalid Fuel ID"
  
  else:
    fuel_instance = get_object_or_404(Fuel, pk=pk)
    try:
      fuel_instance.delete()
      res['status'] = 'success'
      messages.success(request, "Fuel has been deleted successfully")
    except Exception as e:
      res['msg'] = f"Error deleting Fuel: {str(e)}"
  
  return HttpResponse(json.dumps(res), content_type='application/json')

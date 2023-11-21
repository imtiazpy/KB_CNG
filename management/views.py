from django.shortcuts import render
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
def manage_fuel_view(request):
  return render(request, 'management/manage_fuel.html')


@login_required
def add_fuel_view(request):
  res = {'status': 'failed', 'msg': ''}
  if not request.method == 'POST':
    res['msg'] = 'No Data was sent'

  else:
    form = SaveFuelForm(request.POST)

    if form.is_valid():
      form.save()
      messages.success(request, "Fuel has been added successfully")

      res['status'] = 'success'
    else:
      for field in form:
          for error in field.errors:
            if not res['msg'] == '':
                res['msg'] += str('<br />')
            res['msg'] += str(f"[{field.label}] {error}")
  return HttpResponse(json.dumps(res), content_type="application/json")
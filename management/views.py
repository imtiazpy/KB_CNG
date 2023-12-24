from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from django.views import generic
from django.db.models import Sum, Q
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils.decorators import method_decorator
from django.utils import timezone
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
import json
from datetime import datetime

from .models import Product, Stock, Sale
from .forms import SaveFuelForm, SaveStockForm, SaveSaleForm

USER = get_user_model()

class Dashboard(LoginRequiredMixin, generic.View):

  def get(self, request, *args, **kwargs):
    fuels = Product.objects.filter(status=1)
    try:
      total_sale = Sale.objects.filter(fuel__id__in = fuels).aggregate(Sum('total_amount'))['total_amount__sum']
      if total_sale is None:
        total_sale = 0
    except:
      total_sale = 0

    context = {
      'total_fuel_count': fuels.count(),
      'fuels': fuels,
      'total_sale': total_sale,
    }

    return render(request, 'management/dashboard.html', context)

@login_required
def dashboard(request):
  fuels = Fuel.objects.filter(status=1)

  try:
    total_sale = Sale.objects.filter(fuel__id__in = fuels).aggregate(Sum('total_amount'))['total_amount__sum']
    if total_sale is None:
      total_sale = 0
  except:
    total_sale = 0

  context = {
    'total_fuel_count': fuels.count(),
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
  """
  This view is used for rendering form for both addition and editing of the Fuel
  when the pk is passed, the view will be used for editing otherwise create view
  """
  context = {}
  if pk is not None:
    context['fuel'] = Fuel.objects.get(id=pk)
  
  if request.user.is_authenticated:
    context['user'] = request.user.id
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
  """view for both the creation and editing of the fuel"""
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

@login_required
def stock_list_view(request):
  stocks = Stock.objects.all()
  return render(request, 'management/stock_list.html', {'stocks': stocks})

@login_required
def manage_stock_view(request, pk=None):
  """View for rendering form for Addition and Editing of Stock"""
  context = {}
  if pk is not None:
    context['stock'] = Stock.objects.get(id=pk)
  context['fuels'] = Fuel.objects.filter(status=1)
  if request.user.is_authenticated:
    context['user'] = request.user.id
  return render(request, 'management/manage_stock.html', context)


@login_required
def save_stock_view(request, pk=None):
  """view for both the creation and editing of Stock"""

  res = {'status':'failed', 'msg':''}
  if not request.method =='POST':
    res['msg'] = "No data send on this request"
  else:
    post = request.POST
    if post['id'] != '':
      stock = Stock.objects.get(id = post['id'])
      form = SaveStockForm(request.POST, instance=stock)
    else:
      form = SaveStockForm(request.POST)
    if form.is_valid():
      form.save()
      if post['id'] == '':
        messages.success(request, "Stock Record has been added successfully")
      else:
        messages.success(request, "Stock Record has been updated successfully")
      res['status'] = 'success'
    else:
      for field in form:
        for error in field.errors:
          if not res['msg'] == '':
            res['msg'] += str('<br />')
          res['msg'] += str(f"[{field.label}] {error}")
  return HttpResponse(json.dumps(res), content_type="application/json")


@login_required
def stock_detail_view(request, pk=None):
  context = {}
  if pk is not None:
    stock = Stock.objects.get(id=pk)
    context['stock'] = stock
  
  return render(request, 'management/stock_detail.html', context)



@login_required
def stock_delete_view(request, pk=None):
  res = {'status': '', 'msg': ''}
  if pk is None:
    res['msg'] = "Invalid Stock ID"
  
  else:
    stock_instance = get_object_or_404(Stock, pk=pk)
    try:
      stock_instance.delete()
      res['status'] = 'success'
      messages.success(request, "Stock has been deleted successfully")
    except Exception as e:
      res['msg'] = f"Error deleting Stock: {str(e)}"
  
  return HttpResponse(json.dumps(res), content_type='application/json')

@login_required
def inventory_view(request):
  """Inventory listing view"""
  fuels = Fuel.objects.filter(status=1)
  return render(request, 'management/inventory.html', {'fuels': fuels})


@login_required
def sales_list_view(request):
  """Sales listing view"""
  if request.user.is_staff:
    sales = Sale.objects.filter(fuel__status = 1)
  else:
    sales = Sale.objects.filter(manager=request.user, fuel__status = 1)
  return render(request, 'management/sales_list.html', {'sales': sales})


@login_required
def sales_manage_view(request, pk=None):
  """View to render form for both Sales create and edit"""

  context = {}

  if pk is not None:
    context['sale'] = Sale.objects.get(id=pk)
  context['fuels'] = Fuel.objects.filter(status=1)

  if request.user.is_authenticated:
    context['user'] = request.user.id

  return render(request, 'management/manage_sale.html', context)


@login_required
def sales_save_view(request, pk=None):
  """view for Sales create and edit"""

  res = {'status': 'failed', 'msg': ''}

  if request.method != 'POST':
    res['msg'] = 'No data send on this request'
  
  else:
    post = request.POST

    if post['id'] != '':
      sale = Sale.objects.get(id = post['id'])
      form = SaveSaleForm(request.POST, instance=sale)
    else:
      form = SaveSaleForm(request.POST)
    
    if form.is_valid():
      form.save()
      if post['id'] == '':
        messages.success(request, "Sale Record has been added successfully")
      else:
        messages.success(request, "Sale Record has been updated successfully")
      res['status'] = 'success'
    else:
      for field in form:
        for error in field.errors:
          if not res['msg'] == '':
            res['msg'] += str('<br />')
          res['msg'] += str(f"[{field.label}] {error}")
  return JsonResponse(res)

@login_required
def sales_detail_view(request, pk=None):
  context = {}
  if pk is not None:
    context['sale'] = Sale.objects.get(id=pk)
  return render(request, 'management/sale_detail.html', context)


@login_required
def sales_delete_view(request, pk=None):
  res = {'status': '', 'msg': ''}
  if pk is None:
    res['msg'] = "Invalid Sale ID"
  
  else:
    sale_instance = get_object_or_404(Sale, pk=pk)
    try:
      sale_instance.delete()
      res['status'] = 'success'
      messages.success(request, "Sale has been deleted successfully")
    except Exception as e:
      res['msg'] = f"Error deleting Sale: {str(e)}"
  
  return JsonResponse(res)


@login_required
def sales_report_view(request, report_date=None):
  context = {}

  if report_date is not None:
    report_date = datetime.strptime(report_date, "%Y-%m-%d")
  else:
    report_date = datetime.now()
  
  year = report_date.strftime("%Y")
  month = report_date.strftime("%m")
  day = report_date.strftime("%d")

  fuels = Fuel.objects.filter(status=1)
  sales = Sale.objects.filter(manager = request.user, fuel__id__in=fuels, date__month = month, date__day=day, date__year=year)

  context['report_date'] = report_date
  context['sales'] = sales
  context['total_sale'] = sales.aggregate(Sum('total_amount'))['total_amount__sum'] or 0

  return render(request, 'management/sales_report.html', context)



def is_staff_user(user):
  return user.is_staff

@method_decorator(user_passes_test(is_staff_user, login_url=None), name='dispatch')
class SalesReportAdminView(LoginRequiredMixin, generic.ListView):
  model = Sale
  template_name = 'management/sales_report_admin.html'
  context_object_name = 'sales'
  queryset = Sale.objects.all()

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    filtered_sale = self.get_queryset()
    user = self.request.GET.get('user')
    context['users'] = USER.objects.filter(is_active=True)
    context['selected_date'] = self.request.GET.get('date', datetime.now().strftime('%Y-%m-%d'))
    context['total_sale'] = filtered_sale.aggregate(Sum('total_amount'))['total_amount__sum'] or 0

    if user:
      context['selected_user'] = int(user) if user.isdigit() else user
      context['selected_user_name'] = USER.objects.get(id = user) if user.isdigit() else 'All'

    return context

  def get_queryset(self):
    queryset = super().get_queryset()

    filters = Q(fuel__id__in=Fuel.objects.filter(status=1))

    date = self.request.GET.get('date')
    report_date = timezone.datetime.strptime(date, "%Y-%m-%d") if date else timezone.now()

    user_id = self.request.GET.get('user')
    if user_id and user_id.lower() == 'all':
      pass
    else:
      filters &= Q(manager=user_id)

    if date:
      filters &= Q(date=report_date)

    if filters:
      queryset = queryset.filter(filters)
    
    return queryset

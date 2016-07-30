from django.shortcuts import render
from models import Purchase, Sale
from forms import PurchasesForm, SalesForm

# Create your views here.

#@require_POST
def save_purchase_request(request):
  form_data = PurchasesForm(request.POST)
  if form_data.is_valid():
    form_data.save()
    result = 1
  else:
    result = 0

  return render(request, 'requests/templates/requests/response.html', {result: result}, content_type = 'text/html')

#@require_POST
def save_sale_request(request):
  form_data = SalesForm(request.POST)
  if form_data.is_valid():
    form_data.save()
    result = 1
  else:
    result = 0
   
  return render(request, 'requests/templates/requests/response.html', {result: result}, content_type = 'text/html')


  

  

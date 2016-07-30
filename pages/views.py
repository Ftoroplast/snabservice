# -*- coding: utf-8

from django.shortcuts import render
from django.http import HttpResponse
from requests.models import Product, Sale, Purchase
from pages.models import Vacancie

# Create your views here.

def IndexView(request):
  return render(request, 'pages/index.html', context = {}, content_type = 'text/html')

def SalesView(request):
  products = Product.objects.all()

  categories = []
  categories_check_list = []
  for product in products:
    if not (product.category in categories_check_list):
      categories_check_list.append(product.category)
      category = {
        'name': product.category,
        'products': Product.objects.filter(category = product.category).order_by('-shape')
      }
      categories.append(category)

  titles = []
  for product in products:
    if not (product.title in titles):
      titles.append(product.title)
    
  return render(request, 'pages/services__sale.html', context = {'titles': titles, 'categories': categories}, content_type = 'text/html')

def PurchasesView(request):
  return render(request, 'pages/services__purchase.html', context = {}, content_type = 'text/html')

def VacanciesView(request):
  vacancies = Vacancie.objects.all()
  return render(request, 'pages/vacancies.html', context = {'vacancies': vacancies}, content_type = 'text/html')

def ContactsView(request):
  return render(request, 'pages/contacts.html', context = {}, content_type = 'text/html')
   


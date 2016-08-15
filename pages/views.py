# -*- coding: utf-8

import magic
import tempfile
import os

from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.views.decorators.http import require_POST

# Create your views here.
from django.core.mail import EmailMessage
from pages.forms import AddSaleForm, AddContactsForm, AddPurchasesForm, AddVacanciesForm
from pages.models import Vacancie, Product

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

  form_data = AddSaleForm()

  if request.method == 'POST':
    form_data = AddSaleForm(request.POST, request.FILES)
  
    if form_data.is_valid():
      subject = 'Заказ металлолома: ' + form_data.cleaned_data['last_name'].encode('utf-8') + ' ' + form_data.cleaned_data['first_name'].encode('utf-8') + ' ' + form_data.cleaned_data['patronym'].encode('utf-8')
  
      message = 'Имя: ' + form_data.cleaned_data['first_name'].encode('utf-8') + '\n'
      message += 'Отчество: ' + form_data.cleaned_data['patronym'].encode('utf-8') + '\n'
      message += 'Фамилия: ' + form_data.cleaned_data['last_name'].encode('utf-8') + '\n' + '\n'
  
      message += 'Способ доставки: ' + form_data.cleaned_data['delivery_type'].encode('utf-8') + '\n'
      if form_data.cleaned_data['delivery_type'].encode('utf-8') == 'Железной дорогой':
        message += 'Станция: ' + form_data.cleaned_data['station'].encode('utf-8') + '\n' + '\n'
      elif form_data.cleaned_data['delivery_type'].encode('utf-8') == 'Автотранспортом':
        message += 'Адрес: ' + form_data.cleaned_data['address'].encode('utf-8') + '\n' + '\n'
      else:
        message += '\n'
  
      if form_data.cleaned_data['message'].encode('utf-8'):
        message += 'Сообщение: ' + form_data.cleaned_data['message'].encode('utf-8') + '\n' + '\n'
  
      message += 'Выбранные позиции (Идентификатор - Количество в тоннах):' + '\n'
      for key in request.POST:
        if key.find('amount') != -1:
          message += key.split('_')[1].encode('utf-8') + ' - ' + request.POST[key].encode('utf-8') + '\n'
      sender = 'snab-service.com@yandex.ru'
      recipient = ['snabservis_llc@mail.ru']
      email = EmailMessage(subject=subject,body=message,from_email=sender,to=recipient)
  
      cleaned_files = []
      for key in form_data.cleaned_data:
        if key.find('document') != -1 and form_data.cleaned_data[key]:
          cleaned_files.append(form_data.cleaned_data[key])
  
      for document in cleaned_files:
        mime = magic.Magic(mime=True)
        file_mime_type = mime.from_buffer(document.read())
        email.attach(document.name, document.read(), file_mime_type)
  
      email.send(fail_silently = False)
  
      return HttpResponseRedirect('/sales/')
    
  return render(request, 'pages/services__sale.html', context = {'titles': titles, 'categories': categories, 'form': form_data}, content_type = 'text/html')

def PurchasesView(request):
  form_data = AddPurchasesForm()
  
  if request.method == 'POST':
    form_data = AddPurchasesForm(request.POST, request.FILES)
    
    if form_data.is_valid():
      subject = 'Заявка на продажу своего металлолома'
      sender = 'snab-service.com@yandex.ru'
      recipient = ['snabservis_llc@mail.ru']

      message = 'Имя: ' + form_data.cleaned_data['first_name'].encode('utf-8') + '\n'
      message += 'Отчество: ' + form_data.cleaned_data['patronym'].encode('utf-8') + '\n'
      message += 'Фамилия: ' + form_data.cleaned_data['last_name'].encode('utf-8') + '\n' + '\n'

      message += 'Телефон: ' + form_data.cleaned_data['phone'].encode('utf-8') + '\n'
      message += 'E-mail: ' + form_data.cleaned_data['email'].encode('utf-8') + '\n' + '\n'

      if form_data.cleaned_data['city'].encode('utf-8'):
        message += 'Город: ' + form_data.cleaned_data['city'].encode('utf-8') + '\n' + '\n'

      if form_data.cleaned_data['amount'].encode('utf-8'):
        message += 'Количество: ' + form_data.cleaned_data['amount'].encode('utf-8') + '\n' + '\n'

      if form_data.cleaned_data['categories']:
        message += 'Категории: ' 
        for category in form_data.cleaned_data['categories']:
          message += category.encode('utf-8') + ', '
        message = message[0:-2] + '\n' + '\n'
       
      if form_data.cleaned_data['deliverable'].encode('utf-8'):
        message += 'Возможность доставки: ' + form_data.cleaned_data['deliverable'].encode('utf-8') + '\n'
      if form_data.cleaned_data['delivery_type'].encode('utf-8'):
        message += 'Способ доставки: ' + form_data.cleaned_data['delivery_type'].encode('utf-8') + '\n' + '\n'
      else:
        message += '\n'

      if form_data.cleaned_data['message'].encode('utf-8'):
        message += 'Сообщение: ' + form_data.cleaned_data['message'].encode('utf-8')

      email = EmailMessage(subject=subject,body=message,from_email=sender,to=recipient)

      cleaned_files = []
      for key in form_data.cleaned_data:
        if key.find('document') != -1 and form_data.cleaned_data[key]:
          cleaned_files.append(form_data.cleaned_data[key])

      for document in cleaned_files:
        mime = magic.Magic(mime=True)
        file_mime_type = mime.from_buffer(document.read())
        email.attach(document.name, document.read(), file_mime_type)

      email.send(fail_silently = False)

      return HttpResponseRedirect('/purchases/')

  return render(request, 'pages/services__purchase.html', context = {'form': form_data}, content_type = 'text/html')

def VacanciesView(request):
  vacancies = Vacancie.objects.all()
  form_data = AddVacanciesForm()
  
  if request.method == 'POST':
    form_data = AddVacanciesForm(request.POST, request.FILES)
    if form_data.is_valid():
      subject = 'Отклик на вакансию ' + form_data.cleaned_data['vacancie'].encode('utf-8')
      recipient = ['snabservis_llc@mail.ru']
      sender = 'snab-service.com@yandex.ru'

      message = 'Имя: ' + form_data.cleaned_data['first_name'].encode('utf-8') + '\n'
      message += 'Отчество: ' + form_data.cleaned_data['patronym'].encode('utf-8') + '\n'
      message += 'Фамилия: ' + form_data.cleaned_data['last_name'].encode('utf-8') + '\n' + '\n'

      message += 'Телефон: ' + form_data.cleaned_data['phone'].encode('utf-8') + '\n'
      message += 'E-mail: ' + form_data.cleaned_data['email'].encode('utf-8') + '\n' + '\n'

      if form_data.cleaned_data['city'].encode('utf-8'):
        message += 'Город: ' + form_data.cleaned_data['city'].encode('utf-8') + '\n'

      if form_data.cleaned_data['street'].encode('utf-8'):
        message += 'Улица: ' + form_data.cleaned_data['street'].encode('utf-8') + '\n' + '\n'
      else:
        message += '\n'

      message += 'Вакансия: ' + form_data.cleaned_data['vacancie'].encode('utf-8') + '\n' + '\n'

      if form_data.cleaned_data['message'].encode('utf-8'):
        message += 'Сообщение: ' + form_data.cleaned_data['message'].encode('utf-8')

      email = EmailMessage(subject=subject, body=message, from_email=sender, to=recipient)

      cleaned_files = []
      for key in form_data.cleaned_data:
        if key.find('document') != -1 and form_data.cleaned_data[key]:
          cleaned_files.append(form_data.cleaned_data[key])

      for document in cleaned_files:
        mime = magic.Magic(mime=True)
        file_mime_type = mime.from_buffer(document.read())
        email.attach(document.name, document.read(), file_mime_type)

      email.send(fail_silently=False)

      return HttpResponseRedirect('/vacancies/')

  return render(request, 'pages/vacancies.html', context = {'vacancies': vacancies, 'form': form_data}, content_type = 'text/html')

def ContactsView(request):
  form_data = AddContactsForm()

  if request.method == 'POST':
    form_data = AddContactsForm(request.POST)
    
    if form_data.is_valid():
      subject = 'Форма обратной связи'
      recipient = ['snabservis_llc@mail.ru']
      sender = 'snab-service.com@yandex.ru'

      message = 'Имя: ' + form_data.cleaned_data['name'].encode('utf-8') + '\n'
      if form_data.cleaned_data['phone'].encode('utf-8'):
        message += 'Телефон: ' + form_data.cleaned_data['phone'].encode('utf-8') + '\n'
      message += 'Email: ' + form_data.cleaned_data['email'].encode('utf-8') + '\n'
      if form_data.cleaned_data['message'].encode('utf-8'):
        message += 'Сообщение: ' + form_data.cleaned_data['message'].encode('utf-8')

      email = EmailMessage(subject=subject, body=message, from_email=sender, to=recipient)
      email.send(fail_silently=False)

      return HttpResponseRedirect('/contacts/')

  return render(request, 'pages/contacts.html', context = {'form': form_data}, content_type = 'text/html')
   


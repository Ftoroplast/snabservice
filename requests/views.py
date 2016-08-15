# -*- coding: utf-8
import magic
import tempfile
import os

from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.views.decorators.http import require_POST

# Create your views here.
from django.core.mail import EmailMessage
from requests.forms import AddSaleForm, AddContactsForm
from requests.models import SaleOrder

@require_POST
def receive_sale_form(request):
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
    recipient = ['snab-service.com@yandex.ru']
    user = 'snab-service.com@yandex.ru'
    password = 'SnabServiceLLC'
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
           
  return render(request, 'pages/services__sale.html', {'form': form_data})

@require_POST
def receive_contacts_form(request):
  form_data = AddContactsForm(request.POST)
  
  if form_data.is_valid():
    open('log.txt', 'w').write('OK')
    subject = 'Форма обратной связи'
    message = ''
    for key in form_data.cleaned_data:
      message += key + ': ' + form_data.cleaned_data[key].encode('utf-8') + '\n'
    sender = 'snab-service.com@yandex.ru'
    recipient = ['snab-service.com@yandex.ru']
    email = EmailMessage(subject=subject,body=message,from_email=sender,to=recipient)
    email.send(fail_silently = False)
    
  return HttpResponseRedirect('/contacts/')
  
  

  

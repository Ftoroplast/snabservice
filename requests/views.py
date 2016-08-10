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
    message = ''
    for key in form_data.cleaned_data:
      if key != 'documents':
        message += key + ': ' + form_data.cleaned_data[key].encode('utf-8') + '\n'
    sender = 'snab-service.com@yandex.ru'
    recipient = ['snab-service@mail.ru']
    user = 'snab-service.com@yandex.ru'
    password = 'SnabServiceLLC'
    email = EmailMessage(subject=subject,body=message,from_email=sender,to=recipient) 
    for document in request.FILES.getlist('documents'):
      mime = magic.Magic(mime=True)
      file_mime_type = mime.from_buffer(document.read())
      
      if file_mime_type.split('/')[0] == 'image' or file_mime_type == 'application/pdf':
        email.attach(document.name, document.read(), file_mime_type)

    email.send(fail_silently = False)
           
  return HttpResponsRedirect('/sales/')

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
  
  

  

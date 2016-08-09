# -*- coding: utf-8

from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.views.decorators.http import require_POST

# Create your views here.
from django.core.mail import EmailMessage
from requests.forms import AddSaleForm

@require_POST
def receive_sale_form(request):
  form_data = AddSaleForm(request.POST, request.FILES)

  if form_data.is_valid():
    open('log.txt', 'w').write(str(request.FILES))
    subject = u'Заказ металлолома: ' + form_data.cleaned_data['last_name'].encode('utf-8') + ' ' + form_data.cleaned_data['first_name'].encode('utf-8') + ' ' + form_data.cleaned_data['patronym'].encode('utf-8')
    message = ''
    for key in form_data.cleaned_data:
      if key != 'documents':
        message += key + ': ' + form_data.cleaned_data[key].encode('utf-8') + '\n'
    sender = 'snab-service.com@yandex.ru'
    recipient = ['snab-service.com@yandex.ru']
    user = 'snab-service.com@yandex.ru'
    password = 'SnabServiceLLC'
    email = EmailMessage(subject=subject,body=message,from_email=sender,to=recipient) 
    email.attach_file('uploads/sales/' + request.FILES['documents'].name)
    email.send(fail_silently = False)
           
    return HttpResponse('OK')
  else:
    open('log.txt', 'w').write(str(form_data))
    return HttpResponse('Invalid data')



  

  

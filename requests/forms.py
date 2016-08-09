# -*- coding: utf-8

from django import forms
from django.core.mail import send_mail

# Create the form class.
class AddSaleForm(forms.Form):
  last_name = forms.CharField(max_length = 30)
  first_name = forms.CharField(max_length = 30)
  patronym = forms.CharField(max_length = 30)
  delivery_type = forms.ChoiceField(choices = ((u'Самовывозом', u'Самовывозом'), (u'Железной дорогой', u'Железной дорогой'), (u'Автотранспортом', u'Автотранспортом')))
  station = forms.CharField(max_length = 30, required = False)
  address = forms.CharField(max_length = 100, widget = forms.Textarea, required = False)
  message = forms.CharField(max_length = 200, widget = forms.Textarea, required = False)
  documents = forms.FileField()

  def clean(self):
    open('log.txt', 'a').write('yes')
    cleaned_data = super(AddSaleForm, self).clean()
    if cleaned_data['delivery_type'].encode('utf-8') == 'Железной дорогой' and not cleaned_data['station'].encode('utf-8'):
      raise forms.ValidationError(u'Укажите станцию')
    elif cleaned_data['delivery_type'].encode('utf-8') == 'Автотранспортом' and not cleaned_data['address'].encode('utf-8'):
      raise forms.ValidationError(u'Укажите адрес')

#  def mail(self):
#    if (self.is_valid()):
#      open('log.txt', 'a').write('val')
#      subject = 'Заказ металлолома: ' + self.cleaned_data['last_name'] + ' ' + self.cleaned_data['first_name'] + ' ' + self.cleaned_data['patronym']
#      message = ''  
#      for key in self.cleaned_data:
#        message += key + ': ' + self.cleaned_data['key'] + '\n'
#      sender = 'snab-service.com@yandex.ru'
#      recipient = ['snab-service.com@yandex.ru']
#      user = 'snab-service.com@yandex.ru'
#      password = 'SnabServiceLLC'     
      
#      return send_mail(subject=subject,message=message,from_email=sender,recipient_list=recipient,auth_user=user,auth_password=password,fail_silently=False)
        

    

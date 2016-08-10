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
  documents = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))

  def clean(self):
    cleaned_data = super(AddSaleForm, self).clean()
    if cleaned_data['delivery_type'].encode('utf-8') == 'Железной дорогой' and not cleaned_data['station'].encode('utf-8'):
      raise forms.ValidationError(u'Укажите станцию')
    elif cleaned_data['delivery_type'].encode('utf-8') == 'Автотранспортом' and not cleaned_data['address'].encode('utf-8'):
      raise forms.ValidationError(u'Укажите адрес')

class AddContactsForm(forms.Form):
  name = forms.CharField(max_length = 100)
  phone = forms.CharField(max_length = 20, required = False)
  email = forms.EmailField()
  message = forms.CharField(widget = forms.Textarea, required = False) 

    

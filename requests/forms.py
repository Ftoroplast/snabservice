# -*- coding: utf-8

from django import forms

# Create the form class.
class AddSaleForm(forms.Form):
  last_name = forms.CharField(max_length = 30)
  first_name = forms.CharField(max_length = 30)
  patronym = forms.CharField(max_length = 30)
  phone = forms.CharField(max_length = 30)
  email = forms.EmailField(max_length = 40)
  delivery_type = forms.ChoiceField([('Самовывозом', 'Самовывозом'), ('Железной дорогой', 'Железной дорогой'), ('Автотранспортом', 'Автотранспортом')])
  station = forms.CharField(max_length = 30)
  address = forms.CharField(widget = forms.Textarea)
  message = forms.CharField(widget = forms.Textarea)
  documents = forms.FileField()
  

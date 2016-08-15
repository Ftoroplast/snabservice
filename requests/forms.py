# -*- coding: utf-8

from django import forms
from django.core.mail import send_mail

import magic

# Create the form class.
class AddSaleForm(forms.Form):
  last_name = forms.CharField(max_length = 30)
  first_name = forms.CharField(max_length = 30)
  patronym = forms.CharField(max_length = 30)
  delivery_type = forms.ChoiceField(choices = ((u'Самовывозом', u'Самовывозом'), (u'Железной дорогой', u'Железной дорогой'), (u'Автотранспортом', u'Автотранспортом')))
  station = forms.CharField(max_length = 30, required = False)
  address = forms.CharField(max_length = 100, widget = forms.Textarea, required = False)
  message = forms.CharField(max_length = 200, widget = forms.Textarea, required = False)
  document1 = forms.FileField()
  document2 = forms.FileField(required = False)

  def clean(self):
    cleaned_data = super(AddSaleForm, self).clean()
    if 'delivery_type' in cleaned_data:
      if cleaned_data['delivery_type'].encode('utf-8') == 'Железной дорогой' and not cleaned_data['station'].encode('utf-8'):
        raise forms.ValidationError(u'Укажите станцию')
      elif cleaned_data['delivery_type'].encode('utf-8') == 'Автотранспортом' and not cleaned_data['address'].encode('utf-8'):
        raise forms.ValidationError(u'Укажите адрес')
    else:
      raise forms.ValidationError(u'Укажите способ доставки')

    cleaned_files = []
    for key in cleaned_data:
      if key.find('document') != -1 and cleaned_data[key]:
        cleaned_files.append(cleaned_data[key])
        open('cleanedfiles.txt', 'a').write(str(cleaned_data[key]))

    for document in cleaned_files:
      mime = magic.Magic(mime=True)
      file_mime_type = mime.from_buffer(document.read())
      open('filemimetypes.txt', 'a').write(str(file_mime_type))
      open('size.txt', 'w').write(str(document.size))

      if not (file_mime_type == 'application/pdf' or file_mime_type == 'image/jpeg' or file_mime_type == 'image/png' or file_mime_type == 'application/msword' or file_mime_type == 'application/zip') or document.size > 2000000:
        raise forms.ValidationError(u'Допустимые форматы файлов: pdf, doc, jpg, png, zip.\nМаксимальный размер файла: 2МБ.')


class AddContactsForm(forms.Form):
  name = forms.CharField(max_length = 100)
  phone = forms.CharField(max_length = 20, required = False)
  email = forms.EmailField()
  message = forms.CharField(widget = forms.Textarea, required = False) 

    

from django.forms import ModelForm
from requests.models import Purchase, Sale

# Create the form class.
class PurchasesForm(ModelForm):
  class Meta:
    model = Purchase
    fields = ['first_name', 'patronym', 'last_name', 'phone', 'email', 'amount', 'city', 'deliverable', 'delivery_type', 'station_code',
      'scrap_type', 'scrap_media', 'message']

class SalesForm(ModelForm):
  class Meta:
    model = Sale
    fields = ['first_name', 'patronym', 'last_name', 'phone', 'email', 'product', 'delivery_type', 'document', 'message']

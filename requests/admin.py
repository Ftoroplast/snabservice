from django.contrib import admin

from requests.models import Purchase, Sale, Product

# Register your models here.

admin.site.register(Purchase)
admin.site.register(Sale)
admin.site.register(Product)


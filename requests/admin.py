from django.contrib import admin

from requests.models import Purchase, SaleOrder, SaleItem, Product

# Register your models here.

admin.site.register(Purchase)
admin.site.register(SaleOrder)
admin.site.register(Product)
admin.site.register(SaleItem)


# -*- coding: utf-8

from __future__ import unicode_literals

from django.db import models

# Create your models here.

DELIVERY_TYPE_CHOICES = (
  ('самовывозом', 'самовывозом'),
  ('автотранспортом', 'автотранспортом'),
  ('железной дорогой', 'железной дорогой')
)

SCRAP_TYPE_CHOICES = (

)

CITIES = (

)

class Product(models.Model):
  title = models.CharField(max_length = 50, blank = True, default = "none")
  category = models.CharField(max_length = 15, blank = True, default = "none")
  shape = models.CharField(max_length = 30, blank = True, default = 0)
  diameter = models.FloatField(blank = True, default = 0)
  length = models.FloatField(blank = True, default = 0)
  price = models.IntegerField(blank = True, default = 0)

  def __unicode__(self):
    return self.title

class Purchase(models.Model):
  first_name = models.CharField(max_length = 30)
  patronym = models.CharField(max_length = 30)
  last_name = models.CharField(max_length = 30)
  phone = models.CharField(max_length = 30)
  email = models.EmailField()
  amount = models.IntegerField()
  city = models.CharField(max_length = 30, choices = CITIES)
  deliverable = models.BooleanField()
  delivery_type = models.CharField(max_length = 5, choices = DELIVERY_TYPE_CHOICES)
  station_code = models.CharField(max_length = 30)
  scrap_type = models.CharField(max_length = 30, choices = SCRAP_TYPE_CHOICES)
  scrap_media = models.FileField(upload_to = "uploads/purchases")
  message = models.TextField()

  def __unicode__(self):
    return self.first_name + self.patronym + self.last_name

class SaleOrder(models.Model):
  first_name = models.CharField(max_length = 30)
  patronym = models.CharField(max_length = 30)
  last_name = models.CharField(max_length = 30)
  phone = models.CharField(max_length = 30)
  email = models.EmailField()
  delivery_type = models.CharField(max_length = 20, choices = DELIVERY_TYPE_CHOICES)
  document = models.FileField(upload_to = "uploads/sales")
  message = models.TextField()

  def __unicode__(self):
    return str(self.pk)

class SaleItem(models.Model):
  order = models.ForeignKey(SaleOrder)
  product = models.ForeignKey(Product)
  amount = models.IntegerField()

  def __unicode__(self):
    return str(self.order)

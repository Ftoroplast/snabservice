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
  title = models.CharField(max_length = 50)
  category = models.CharField(max_length = 15)
  shape = models.CharField(max_length = 30, blank = True, default = 0)
  diameter = models.DecimalField(max_digits = 10, decimal_places = 5)
  length = models.DecimalField(max_digits = 10, decimal_places = 5, blank = True, default = 0)
  price = models.IntegerField()

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

class Sale(models.Model):
  first_name = models.CharField(max_length = 30)
  patronym = models.CharField(max_length = 30)
  last_name = models.CharField(max_length = 30)
  phone = models.CharField(max_length = 30)
  email = models.EmailField()
  product = models.ManyToManyField(Product)
  delivery_type = models.CharField(max_length = 20, choices = DELIVERY_TYPE_CHOICES)
  document = models.FileField(upload_to = "uploads/sales")
  message = models.TextField()

  def __unicode__(self):
    return self.first_name + self.patronym + self.last_name

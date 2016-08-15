# -*- coding: utf-8

from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Vacancie(models.Model):
  position = models.CharField(max_length = 50)
  schedule = models.CharField(max_length = 50)
  responsibility = models.TextField()
  work_place = models.CharField(max_length = 50)
  salary = models.CharField(max_length = 50)

class Product(models.Model):
  title = models.CharField(max_length = 50, blank = True, default = "none")
  category = models.CharField(max_length = 15, blank = True, default = "none")
  shape = models.CharField(max_length = 30, blank = True, default = 0)
  diameter = models.FloatField(blank = True, default = 0)
  length = models.FloatField(blank = True, default = 0)
  price = models.IntegerField(blank = True, default = 0)
 
  def __unicode__(self):
    return self.title

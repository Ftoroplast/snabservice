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

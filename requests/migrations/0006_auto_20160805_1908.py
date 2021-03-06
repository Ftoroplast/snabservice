# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-05 19:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('requests', '0005_auto_20160804_2204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(blank=True, default='none', max_length=15),
        ),
        migrations.AlterField(
            model_name='product',
            name='diameter',
            field=models.FloatField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='product',
            name='title',
            field=models.CharField(blank=True, default='none', max_length=50),
        ),
    ]

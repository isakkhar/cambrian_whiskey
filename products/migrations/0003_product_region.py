# -*- coding: utf-8 -*-
# Generated by Django 1.11.28 on 2020-04-20 13:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='region',
            field=models.CharField(choices=[('europe', 'europe'), ('america', 'america'), ('rest_of_world', 'rest_of_world')], default='europe', max_length=13),
        ),
    ]

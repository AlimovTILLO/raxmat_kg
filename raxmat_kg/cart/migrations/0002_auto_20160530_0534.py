# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-05-30 05:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cartitem',
            options={'ordering': ('cart',), 'verbose_name': 'cartitem', 'verbose_name_plural': 'cartitems'},
        ),
    ]

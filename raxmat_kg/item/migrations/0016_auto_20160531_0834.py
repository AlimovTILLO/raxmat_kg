# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-05-31 08:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0015_auto_20160531_0807'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='item_category_id',
            new_name='item_category',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='item_charity_id',
            new_name='item_charity',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='item_foundation_id',
            new_name='item_foundation',
        ),
        migrations.RenameField(
            model_name='itemcategory',
            old_name='item_category_main_id',
            new_name='item_category_main',
        ),
    ]

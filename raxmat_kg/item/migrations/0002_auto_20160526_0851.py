# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-05-26 08:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='item_image',
            field=models.ImageField(null=0, upload_to=b''),
        ),
    ]

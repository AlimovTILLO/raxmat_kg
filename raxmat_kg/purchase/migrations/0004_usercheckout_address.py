# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-06-19 12:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchase', '0003_auto_20160619_1731'),
    ]

    operations = [
        migrations.AddField(
            model_name='usercheckout',
            name='address',
            field=models.CharField(max_length=200, null=True),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-05-27 14:38
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('foundation', '0001_initial'),
        ('item', '0008_auto_20160527_1044'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='item_charity_id',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='item',
            name='item_foundation_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='foundation.Foundation'),
        ),
        migrations.AddField(
            model_name='item',
            name='item_price',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='comments',
            name='comments_from',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='comments',
            name='comments_item',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='item.Item'),
        ),
    ]
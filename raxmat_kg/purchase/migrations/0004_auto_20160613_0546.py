# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-06-13 05:46
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('purchase', '0003_auto_20160613_0518'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_data', models.CharField(max_length=50)),
                ('account_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'account',
                'verbose_name': 'account',
                'verbose_name_plural': 'accounts',
            },
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('transaction_status', models.TextField(default=None)),
                ('transaction_from_account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='purchase.Account')),
            ],
            options={
                'db_table': 'transaction',
                'verbose_name': 'transaction',
                'verbose_name_plural': 'transactions',
            },
        ),
        migrations.AlterField(
            model_name='purchase',
            name='purchase_pin',
            field=models.TextField(default=b'a555d'),
        ),
    ]

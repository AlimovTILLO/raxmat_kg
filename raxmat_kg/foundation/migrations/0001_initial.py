# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-06-10 08:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Foundation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foundation_name', models.CharField(max_length=200)),
                ('foundation_description', models.TextField()),
                ('foundation_logo', models.FileField(blank=True, null=True, upload_to=b'')),
                ('foundation_status', models.CharField(max_length=50, null=True)),
                ('foundation_url', models.URLField(null=True, verbose_name='\u0421\u0441\u044b\u043b\u043a\u0430')),
            ],
            options={
                'db_table': 'foundation',
                'verbose_name': '\u0424\u043e\u043d\u0434',
                'verbose_name_plural': '\u0424\u043e\u043d\u0434\u044b',
            },
        ),
        migrations.CreateModel(
            name='FoundationCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foundation_category_name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'foundation_category',
                'verbose_name': '\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f \u0444\u043e\u043d\u0434\u0430',
                'verbose_name_plural': '\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438 \u0424\u043e\u043d\u0434\u043e\u0432',
            },
        ),
        migrations.AddField(
            model_name='foundation',
            name='foundation_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='foundation.FoundationCategory'),
        ),
    ]

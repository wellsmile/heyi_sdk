# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-26 06:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_remove_app_disabled'),
    ]

    operations = [
        migrations.AddField(
            model_name='app',
            name='version_name',
            field=models.CharField(default='', max_length=128, verbose_name='\u7528\u4e8e\u5448\u73b0\u7ed9\u7528\u6237\u7684\u7248\u672c'),
        ),
    ]

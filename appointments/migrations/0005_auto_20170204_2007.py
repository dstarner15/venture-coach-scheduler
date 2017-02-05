# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-05 01:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0004_auto_20170204_1451'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='email',
            field=models.EmailField(default='', max_length=128),
        ),
        migrations.AddField(
            model_name='appointment',
            name='name',
            field=models.CharField(default='', max_length=128),
        ),
    ]
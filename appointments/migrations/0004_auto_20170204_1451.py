# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-04 19:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0003_auto_20170204_1438'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='type',
            field=models.CharField(choices=[('h__co', 'Venture Coach'), ('h__sf', 'Software Fellow'), ('h__df', 'Design Fellow'), ('us', 'User')], default='us', help_text='Account type.', max_length=5),
        ),
    ]
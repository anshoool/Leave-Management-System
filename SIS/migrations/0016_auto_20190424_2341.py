# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2019-04-24 18:11
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SIS', '0015_auto_20190417_1223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leaverequest',
            name='end',
            field=models.DateField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='leaverequest',
            name='start',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-24 02:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('axf', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wheel',
            name='isDelete',
            field=models.BooleanField(default=True),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-06-15 13:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fastnews', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=77),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-11-10 06:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='show',
            name='desc',
            field=models.TextField(null=True),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-07 19:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='applicationsmv',
            name='comments',
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-06-02 07:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apptours', '0003_auto_20170602_0648'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='StepsConfig',
            new_name='Step',
        ),
    ]

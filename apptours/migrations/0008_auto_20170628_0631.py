# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-06-28 06:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apptours', '0007_tour_state'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tour',
            old_name='state',
            new_name='status',
        ),
    ]

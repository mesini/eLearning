# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-15 17:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_deleteuser'),
    ]

    operations = [
        migrations.CreateModel(
            name='EditUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=30)),
            ],
        ),
    ]

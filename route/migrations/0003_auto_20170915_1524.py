# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-09-15 15:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('route', '0002_grouproutinginfo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grouproutinginfo',
            name='groupname',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='auth.Group'),
        ),
    ]

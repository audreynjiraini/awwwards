# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2019-10-21 19:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Profile'),
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-22 18:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventSystem', '0002_event'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='guests',
            field=models.ManyToManyField(related_name='guests', to='eventSystem.User'),
        ),
        migrations.AddField(
            model_name='event',
            name='owners',
            field=models.ManyToManyField(related_name='owners', to='eventSystem.User'),
        ),
        migrations.AddField(
            model_name='event',
            name='vendors',
            field=models.ManyToManyField(related_name='vendors', to='eventSystem.User'),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-22 18:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventSystem', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eventname', models.CharField(max_length=100)),
                ('date_time', models.DateTimeField(verbose_name='when')),
            ],
        ),
    ]

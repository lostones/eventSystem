# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-02 21:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventSystem', '0015_auto_20170302_0135'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choiceresponse',
            name='response_value',
        ),
        migrations.AddField(
            model_name='choiceresponse',
            name='response_value',
            field=models.ManyToManyField(related_name='choices', to='eventSystem.Question'),
        ),
    ]

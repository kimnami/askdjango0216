# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-31 01:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webtoon', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='webtoon',
            options={'ordering': ['-id']},
        ),
    ]

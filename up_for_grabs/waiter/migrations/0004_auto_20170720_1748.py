# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-21 00:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('waiter', '0003_auto_20170720_2338'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='owner_name',
            new_name='name',
        ),
    ]

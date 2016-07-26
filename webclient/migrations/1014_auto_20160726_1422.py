# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-26 14:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webclient', '1013_auto_20160726_1209'),
    ]

    operations = [
        migrations.RenameField(
            model_name='imagewindow',
            old_name='width',
            new_name='height',
        ),
        migrations.AlterUniqueTogether(
            name='imagewindow',
            unique_together=set([('x', 'y', 'length', 'height')]),
        ),
    ]
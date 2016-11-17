# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-17 14:53
from __future__ import unicode_literals

from django.db import migrations
import russian_fields.territory_code


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_samplemodel_agency_type_esia'),
    ]

    operations = [
        migrations.AddField(
            model_name='samplemodel',
            name='territory_code',
            field=russian_fields.territory_code.TerritoryCodeField(blank=True, null=True),
        ),
    ]
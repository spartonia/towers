# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('visualization', '0004_auto_20160213_0406'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gadm2',
            name='geom',
            field=django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326),
        ),
    ]

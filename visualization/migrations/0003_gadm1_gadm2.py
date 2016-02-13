# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('visualization', '0002_remove_gadm_enabled'),
    ]

    operations = [
        migrations.CreateModel(
            name='GADM1',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('enabled', models.BooleanField(default=False)),
                ('id_0', models.IntegerField()),
                ('iso', models.CharField(max_length=3)),
                ('name_0', models.CharField(max_length=75)),
                ('id_1', models.IntegerField()),
                ('name_1', models.CharField(max_length=75)),
                ('hasc_1', models.CharField(max_length=15)),
                ('ccn_1', models.IntegerField()),
                ('cca_1', models.CharField(max_length=254)),
                ('type_1', models.CharField(max_length=50)),
                ('engtype_1', models.CharField(max_length=50)),
                ('nl_name_1', models.CharField(max_length=50)),
                ('varname_1', models.CharField(max_length=150)),
                ('geom', django.contrib.gis.db.models.fields.PolygonField(srid=4326)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='GADM2',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('enabled', models.BooleanField(default=False)),
                ('id_0', models.IntegerField()),
                ('iso', models.CharField(max_length=3)),
                ('name_0', models.CharField(max_length=75)),
                ('id_1', models.IntegerField()),
                ('name_1', models.CharField(max_length=75)),
                ('id_2', models.IntegerField()),
                ('name_2', models.CharField(max_length=75)),
                ('hasc_2', models.CharField(max_length=15)),
                ('ccn_2', models.IntegerField()),
                ('cca_2', models.CharField(max_length=254)),
                ('type_2', models.CharField(max_length=50)),
                ('engtype_2', models.CharField(max_length=50)),
                ('nl_name_2', models.CharField(max_length=75)),
                ('varname_2', models.CharField(max_length=150)),
                ('geom', django.contrib.gis.db.models.fields.PolygonField(srid=4326)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]

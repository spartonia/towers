# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GADM',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('enabled', models.BooleanField(default=False)),
                ('id_0', models.IntegerField()),
                ('iso', models.CharField(max_length=3)),
                ('name_engli', models.CharField(max_length=50)),
                ('name_iso', models.CharField(max_length=54)),
                ('name_fao', models.CharField(max_length=50)),
                ('name_local', models.CharField(max_length=54)),
                ('name_obsol', models.CharField(max_length=150)),
                ('name_varia', models.CharField(max_length=160)),
                ('name_nonla', models.CharField(max_length=50)),
                ('name_frenc', models.CharField(max_length=50)),
                ('name_spani', models.CharField(max_length=50)),
                ('name_russi', models.CharField(max_length=50)),
                ('name_arabi', models.CharField(max_length=50)),
                ('name_chine', models.CharField(max_length=50)),
                ('waspartof', models.CharField(max_length=100)),
                ('contains', models.CharField(max_length=50)),
                ('sovereign', models.CharField(max_length=40)),
                ('iso2', models.CharField(max_length=4)),
                ('www', models.CharField(max_length=2)),
                ('fips', models.CharField(max_length=6)),
                ('ison', models.FloatField()),
                ('validfr', models.CharField(max_length=12)),
                ('validto', models.CharField(max_length=10)),
                ('pop2000', models.FloatField()),
                ('sqkm', models.FloatField()),
                ('popsqkm', models.FloatField()),
                ('unregion1', models.CharField(max_length=254)),
                ('unregion2', models.CharField(max_length=254)),
                ('developing', models.FloatField()),
                ('cis', models.FloatField()),
                ('transition', models.FloatField()),
                ('oecd', models.FloatField()),
                ('wbregion', models.CharField(max_length=254)),
                ('wbincome', models.CharField(max_length=254)),
                ('wbdebt', models.CharField(max_length=254)),
                ('wbother', models.CharField(max_length=254)),
                ('ceeac', models.FloatField()),
                ('cemac', models.FloatField()),
                ('ceplg', models.FloatField()),
                ('comesa', models.FloatField()),
                ('eac', models.FloatField()),
                ('ecowas', models.FloatField()),
                ('igad', models.FloatField()),
                ('ioc', models.FloatField()),
                ('mru', models.FloatField()),
                ('sacu', models.FloatField()),
                ('uemoa', models.FloatField()),
                ('uma', models.FloatField()),
                ('palop', models.FloatField()),
                ('parta', models.FloatField()),
                ('cacm', models.FloatField()),
                ('eurasec', models.FloatField()),
                ('agadir', models.FloatField()),
                ('saarc', models.FloatField()),
                ('asean', models.FloatField()),
                ('nafta', models.FloatField()),
                ('gcc', models.FloatField()),
                ('csn', models.FloatField()),
                ('caricom', models.FloatField()),
                ('eu', models.FloatField()),
                ('can', models.FloatField()),
                ('acp', models.FloatField()),
                ('landlocked', models.FloatField()),
                ('aosis', models.FloatField()),
                ('sids', models.FloatField()),
                ('islands', models.FloatField()),
                ('ldc', models.FloatField()),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='OpenCellId',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('radio', models.CharField(max_length=10)),
                ('mcc', models.IntegerField()),
                ('net', models.IntegerField()),
                ('area', models.IntegerField()),
                ('cell', models.IntegerField()),
                ('unit', models.IntegerField(null=True)),
                ('lon', models.FloatField()),
                ('lat', models.FloatField()),
                ('range', models.IntegerField()),
                ('samples', models.IntegerField()),
                ('changeable', models.IntegerField()),
                ('created', models.IntegerField()),
                ('updated', models.IntegerField()),
                ('averageSignal', models.IntegerField()),
                ('coord', django.contrib.gis.db.models.fields.PointField(srid=4326, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]

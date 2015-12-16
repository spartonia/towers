from django.db import models


class OpenCellId(models.Model):
    radio = models.CharField(
        max_length=10
    )
    mcc = models.IntegerField()
    net = models.IntegerField()
    area = models.IntegerField()
    cell = models.IntegerField()
    unit = models.IntegerField(
        null=True
    )
    lon = models.FloatField()
    lat = models.FloatField()
    range = models.IntegerField()
    samples = models.IntegerField()
    changeable = models.IntegerField()
    created = models.IntegerField()
    updated = models.IntegerField()
    averageSignal = models.IntegerField()
# Create your models here.
from django.db import models

class Weather(models.Model):
    visibility = models.FloatField(blank=True, null=True)
    dew_pt = models.FloatField(blank=True, null=True)
    QFE = models.FloatField(blank=True, null=True)
    LC = models.FloatField(blank=True, null=True)
    TC = models.FloatField(blank=True, null=True)
    DRY = models.FloatField(blank=True, null=True)
    RH = models.FloatField(blank=True, null=True)
    WET = models.FloatField(blank=True, null=True)
    month = models.FloatField(blank=True, null=True)


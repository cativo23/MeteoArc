 -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Songs(models.Model):
    # song title
    title = models.CharField(max_length=255, null=False)
    # name of artist or group/band
    artist = models.CharField(max_length=255, null=False)

    def __str__(self):
        return "{} - {}".format(self.title, self.artist)


class DatoMeterologico(models.Model):
    humedadDHT11 = models.DecimalField(decimal_places=4, max_digits=10)
    tempDHT11C = models.DecimalField(decimal_places=4, max_digits=10)
    tempDHT11F = models.DecimalField(decimal_places=4, max_digits=10)
    IndCalorDHT11 = models.DecimalField(decimal_places=4, max_digits=10)
    altitudMBMP = models.DecimalField(decimal_places=4, max_digits=10)
    altitudFBMP = models.DecimalField(decimal_places=4, max_digits=10)
    tempBMPC = models.DecimalField(decimal_places=4, max_digits=10)
    tempBMPF = models.DecimalField(decimal_places=4, max_digits=10)
    presionAbsMB = models.DecimalField(decimal_places=4, max_digits=10)
    presionAbsInHg = models.DecimalField(decimal_places=4, max_digits=10)
    presionNivelMarMB = models.DecimalField(decimal_places=4, max_digits=10)
    presionNivelMarInHg = models.DecimalField(decimal_places=4, max_digits=10)
    esDia = models.BooleanField()
    velocidadViento = models.DecimalField(decimal_places=4, max_digits=10)
    direccionViento = models.DecimalField(decimal_places=4, max_digits=10)
    cantidadLLuvia = models.DecimalField(decimal_places=4, max_digits=10)
    fecha = models.DateTimeField(auto_now_add=True, blank=False, null=False)

    def __str__(self):
        return "Dato Meteorologico de: {}".format(self.fecha)

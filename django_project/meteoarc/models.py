# -*- coding: utf-8 -*-
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
    humedadDHT11 = models.DecimalField(decimal_places=2, max_digits=10,default=0.0, null=False)
    tempDHT11C = models.DecimalField(decimal_places=2, max_digits=10,default=0.0, null=False)
    tempDHT11F = models.DecimalField(decimal_places=2, max_digits=10,default=0.0, null=False)
    IndCalorDHT11 = models.DecimalField(decimal_places=2, max_digits=10,default=0.0, null=False)
    altitudMBMP = models.DecimalField(decimal_places=2, max_digits=10,default=0.0, null=False)
    altitudFBMP = models.DecimalField(decimal_places=2, max_digits=10,default=0.0, null=False)
    tempBMPC = models.DecimalField(decimal_places=2, max_digits=10,default=0.0, null=False)
    tempBMPF = models.DecimalField(decimal_places=2, max_digits=10,default=0.0, null=False)
    presionAbsMB = models.DecimalField(decimal_places=2, max_digits=10,default=0.0, null=False)
    presionAbsInHg = models.DecimalField(decimal_places=2, max_digits=10,default=0.0, null=False)
    presionNivelMarMB = models.DecimalField(decimal_places=2, max_digits=10,default=0.0, null=False)
    presionNivelMarInHg = models.DecimalField(decimal_places=2, max_digits=10,default=0.0, null=False)
    esDia = models.BooleanField(default=False, null=False)
    velocidadViento = models.DecimalField(decimal_places=2, max_digits=10,default=0.0, null=False)
    direccionViento = models.CharField(max_length= 10, default="Nada", null=False)
    cantidadLLuvia = models.DecimalField(decimal_places=2, max_digits=10,default=0.0, null=False)
    fecha = models.DateTimeField(auto_now_add=True, blank=False, null=False)

    def __str__(self):
        return "Dato Meteorologico de: {}".format(self.fecha)

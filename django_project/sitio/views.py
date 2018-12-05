# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic.list import ListView
from meteoarc.models import DatoMeterologico

# Create your views here.
class Index(ListView):
    model = DatoMeterologico
    template_name = 'arcindex.html'

    def get_context_data(self, **kwargs):
        context = super(Index, self).get_context_data(**kwargs)
        dato = DatoMeterologico.objects.order_by('-fecha').first()
        soleado = False
        noche = False
        lloviendo= False
        muchoViento = False
        esD = False
        helado = False
        estado = "Esta "
        estado1 = None

        esD = dato.esDia
        tempCDHT11 = dato.tempDHT11C
        if tempCDHT11 >=30:
            if esD:
                soleado = True
                noche =False
            else:
                soleado = False
                noche = True

            helado = False
        else:
            if esD:
                soleado = True
                noche = False
            else:
                soleado = False
                noche = True
            helado = True

        cantLLuvia = dato.cantidadLLuvia
        if cantLLuvia>0:
            lloviendo = True

        cantViento = dato.velocidadViento
        if cantViento>=50:
            muchoViento = True

        if muchoViento:
            estado += "Ventoso "
            estado1 = "Ventoso"

        if soleado:
            estado += "Soleado "
            estado1 = "Soleado"
        elif noche:
            estado += "Noche "
            estado1 = "Noche"

        if lloviendo:
            estado += "Lluvioso "
            estado1 = "Lluvioso"

        if helado:
            estado += "Frío "
            estado1 = "Frío"

        context['estado'] = estado
        context['estado1'] = estado1
        return context

    def get_queryset(self):
        return [DatoMeterologico.objects.order_by('-fecha').first()]

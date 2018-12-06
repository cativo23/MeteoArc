# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic.list import ListView
from meteoarc.models import DatoMeterologico
import datetime
from django.utils import timezone

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
        tempCDHT11 = dato .tempDHT11C
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
        if cantLLuvia>10:
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
            print(cantLLuvia)
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


class Semana(ListView):
    model = DatoMeterologico
    template_name = 'lista.html'

    def get_context_data(self, **kwargs):
        dt = datetime.datetime.now()
        start =  dt.replace(hour=23, minute=59, second=59, microsecond=999999)
        end =  dt - datetime.timedelta(days=7)
        end = end.replace(hour=0, minute=0, second=0, microsecond=0)
        context = super(Semana, self).get_context_data(**kwargs)
        context['titulo'] = "Datos de la Última Semana"
        context['start'] = start
        context['end'] = end
        return context

    def get_queryset(self):
        dt = datetime.datetime.now()
        start =  dt.replace(hour=23, minute=59, second=59, microsecond=999999)
        end =  dt - datetime.timedelta(days=7)
        end = end.replace(hour=0, minute=0, second=0, microsecond=0)
        print(start)
        datos = DatoMeterologico.objects.filter(fecha__range=[end, start])
        return datos

class Mes(ListView):
    model = DatoMeterologico
    template_name = 'lista.html'

    def get_context_data(self, **kwargs):
        dt = datetime.datetime.now()
        start =  dt.replace(hour=23, minute=59, second=59, microsecond=999999)
        end =  dt - datetime.timedelta(days=30)
        end = end.replace(hour=0, minute=0, second=0, microsecond=0)
        context = super(Mes, self).get_context_data(**kwargs)
        context['titulo'] = "Datos de Último Mes"
        context['start'] = start
        context['end'] = end
        return context

    def get_queryset(self):
        dt = datetime.datetime.now()
        start =  dt.replace(hour=23, minute=59, second=59, microsecond=999999)
        end =  dt - datetime.timedelta(days=30)
        end = end.replace(hour=0, minute=0, second=0, microsecond=0)
        print(start)
        datos = DatoMeterologico.objects.filter(fecha__range=[end, start])
        return datos

class Anio(ListView):
    model = DatoMeterologico
    template_name = 'lista.html'

    def get_context_data(self, **kwargs):
        dt = datetime.datetime.now()
        start =  dt.replace(hour=23, minute=59, second=59, microsecond=999999)
        end =  dt - datetime.timedelta(days=360)
        end = end.replace(hour=0, minute=0, second=0, microsecond=0)
        context = super(Anio, self).get_context_data(**kwargs)
        context['titulo'] = "Datos de Último Año"
        context['start'] = start
        context['end'] = end
        return context

    def get_queryset(self):
        dt = datetime.datetime.now()
        start =  dt.replace(hour=23, minute=59, second=59, microsecond=999999)
        end =  dt - datetime.timedelta(days=360)
        end = end.replace(hour=0, minute=0, second=0, microsecond=0)
        print(end)
        datos = DatoMeterologico.objects.filter(fecha__range=[end, start])
        return datos


class Hoy(ListView):
    model = DatoMeterologico
    template_name = 'lista.html'

    def get_context_data(self, **kwargs):
        dt = datetime.datetime.now()
        start =  dt.replace(hour=23, minute=59, second=59, microsecond=999999)
        end = dt.replace(hour=0, minute=0, second=0, microsecond=0)
        context = super(Hoy, self).get_context_data(**kwargs)
        context['titulo'] = "Datos de Hoy"
        context['start'] = start
        context['end'] = end
        return context

    def get_queryset(self):
        dt = datetime.datetime.now()
        start =  dt.replace(hour=23, minute=59, second=59, microsecond=999999)
        end = dt.replace(hour=0, minute=0, second=0, microsecond=0)
        print(end)
        datos = DatoMeterologico.objects.filter(fecha__range=[end, start])
        return datos

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic.list import ListView
from meteoarc.models import DatoMeterologico

# Create your views here.
class Index(ListView):
    model = DatoMeterologico
    template_name = 'sitio/templates/arcindex.html'

    def get_queryset(self):
        return [DatoMeterologico.objects.order_by('-fecha').first()]

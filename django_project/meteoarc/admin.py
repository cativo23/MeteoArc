# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

from .models import Songs, DatoMeterologico

admin.site.register(Songs)
admin.site.register(DatoMeterologico)

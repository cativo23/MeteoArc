from django.conf.urls import url
from .views import Index, Semana, Mes, Anio, Hoy


urlpatterns = [
    url(r'', Index.as_view(), name="indez"),
    url(r'semana/', Semana.as_view(), name="semana"),
    url(r'mes/', Mes.as_view(), name="mes"),
    url(r'anio/', Anio.as_view(), name="anio"),
    url(r'hoy/', Hoy.as_view(), name="hoy"),
]

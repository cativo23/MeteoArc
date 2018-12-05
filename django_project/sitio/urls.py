from django.conf.urls import url
from .views import Index, Semana


urlpatterns = [
    url(r'index/', Index.as_view(), name="index"),
    url(r'semana/', Semana.as_view(), name="semana"),
]

from rest_framework import serializers
from .models import Songs, DatoMeterologico


class SongsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Songs
        fields = ("title", "artist")

class DatoSerializer(serializers.ModelSerializer):

    class Meta:
        model = DatoMeterologico
        fields = ("humedadDHT11","tempDHT11C","tempDHT11F",
        "IndCalorDHT11",
        "altitudMBMP",
        "altitudFBMP",
        "tempBMPC",
        "tempBMPF",
        "presionAbsMB",
        "presionAbsInHg",
        "presionNivelMarMB",
        "presionNivelMarInHg",
        "esDia",
        "velocidadViento",
        "direccionViento",
        "cantidadLLuvia",
        "fecha")

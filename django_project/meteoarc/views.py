# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework import generics
from .models import Songs, DatoMeterologico
from .serializers import SongsSerializer, DatoSerializer
from rest_framework.response import Response
from rest_framework import status


# Create your views here.
class ListSongsView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = Songs.objects.all()
    serializer_class = SongsSerializer


class SongsList(generics.ListCreateAPIView):
    queryset = Songs.objects.all()
    serializer_class = SongsSerializer


class SongDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Songs.objects.all()
    serializer_class = SongsSerializer


class SongPost(generics.CreateAPIView):
    serializer_class = SongsSerializer

    def post(self, request, format=None):
        serializer = SongsSerializer(data=request.data)
        if serializer.is_valid():
            instance = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


class ListDatoView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = DatoMeterologico.objects.all()
    serializer_class = DatoSerializer


class DatoList(generics.ListCreateAPIView):
    queryset = DatoMeterologico.objects.all()
    serializer_class = DatoSerializer


class DatoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = DatoMeterologico.objects.all()
    serializer_class = DatoSerializer


class DatoPost(generics.CreateAPIView):
    serializer_class = DatoSerializer

    def post(self, request, format=None):
        serializer = DatoSerializer(data=request.data)
        if serializer.is_valid():
            instance = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

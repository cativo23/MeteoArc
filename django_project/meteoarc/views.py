# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework import generics
from .models import Songs, DatoMeterologico
from .serializers import SongsSerializer, DatoSerializer
from rest_framework.response import Response
from rest_framework import status
from django.views.generic.list import ListView
from django.utils import timezone



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
    serializer_class = DatoSerializer

    def get_queryset(self):
        return [DatoMeterologico.objects.order_by('-fecha').first()]

    def list(self, request, *args, **kwargs):
        self.object_list = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(self.object_list, many=True)
        return Response({'results': serializer.data})


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

class Index(ListView):
    model = DatoMeterologico
    template_name = 'index.html'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

    def get_queryset(self):
        return [DatoMeterologico.objects.order_by('-fecha').first()]

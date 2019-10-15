from django.shortcuts import render
from rest_framework import viewsets, generics
from iplstats.models import Match, Delivery
from drf_api.serializers import MatchSerializer, DeliverySerializer

class MatchViewSet(generics.ListCreateAPIView):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer

class MatchDetailViewSet(generics.RetrieveUpdateDestroyAPIView):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer

class DeliveryViewSet(generics.ListCreateAPIView):
    queryset = Delivery.objects.all()
    serializer_class = DeliverySerializer

class DeliveryDetailViewSet(generics.RetrieveUpdateDestroyAPIView):
    queryset = Delivery.objects.all()
    serializer_class = DeliverySerializer
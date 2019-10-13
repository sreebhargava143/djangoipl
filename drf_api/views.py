from django.shortcuts import render
from rest_framework import viewsets
from iplstats.models import Match, Delivery
from drf_api.serializers import MatchSerializer, DeliverySerializer
class MatchViewSet(viewsets.ModelViewSet):
    queryset = Match.objects.all().order_by('id')
    serializer_class = MatchSerializer

class DeliveryViewSet(viewsets.ModelViewSet):
    queryset = Delivery.objects.all().order_by('id')
    serializer_class = DeliverySerializer
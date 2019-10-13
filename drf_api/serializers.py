from iplstats.models import Match, Delivery
from rest_framework import serializers

class MatchSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Match
        fields = ['id', 'season', 'team1', 'team2', 'winner']

class DeliverySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Delivery
        fields = ['id', 'match_id', 'batsman', 'bowler']

from iplstats.models import Match, Delivery
from rest_framework import serializers

class MatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = '__all__'
        # fields = ['id', 'season', 'team1', 'team2', 'winner']

class DeliverySerializer(serializers.ModelSerializer):
    class Meta:
        model = Delivery
        fields = '__all__'
        #fields = ['id', 'match_id', 'batsman', 'bowler']

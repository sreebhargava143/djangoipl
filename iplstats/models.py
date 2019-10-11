from django.db import models
from postgres_copy import CopyManager


class Match(models.Model):
    id = models.IntegerField(primary_key=True)
    season = models.IntegerField(null=False)
    city = models.CharField(max_length=60, null=True)
    date = models.DateField(null=False)
    team1 = models.CharField(max_length=60, null=False)
    team2 = models.CharField(max_length=60, null=False)
    toss_winner = models.CharField(max_length=60, null=False)
    toss_decision = models.CharField(max_length=60, null=False)
    result = models.CharField(max_length=60, null=False)
    dl_applied = models.IntegerField(null=False)
    winner = models.CharField(max_length=60, null=True)
    win_by_runs = models.IntegerField(null=True)
    win_by_wickets = models.IntegerField(null=True)
    player_of_match = models.CharField(max_length=60, null=True)
    venue = models.CharField(max_length=60, null=False)
    umpire1 = models.CharField(max_length=60, null=True)
    umpire2 = models.CharField(max_length=60, null=True)
    umpire3 = models.CharField(max_length=60, null=True)
    objects = CopyManager()

    def __str__(self):
        return f'{self.season} , {self.team1} vs {self.team2}'

class Delivery(models.Model):
    match_id = models.ForeignKey(Match, on_delete=models.CASCADE)
    inning = models.IntegerField(null=False)
    batting_team = models.CharField(max_length=60, null=False)
    bowling_team = models.CharField(max_length=60, null=False)
    over = models.IntegerField(null=True)
    ball = models.IntegerField(null=True)
    batsman = models.CharField(max_length=60, null=False)
    non_striker = models.CharField(max_length=60, null=True)
    bowler = models.CharField(max_length=60, null=False)
    is_super_over = models.IntegerField(null=True)
    wide_runs = models.IntegerField(null=True)
    bye_runs = models.IntegerField(null=True)
    legbye_runs = models.IntegerField(null=True)
    noball_runs = models.IntegerField(null=True)
    penalty_runs = models.IntegerField(null=True)
    batsman_runs = models.IntegerField(null=True)
    extra_runs = models.IntegerField(null=True)
    total_runs = models.IntegerField(null=True)
    player_dismissed = models.CharField(max_length=60, null=True)
    dismissal_kind = models.CharField(max_length=60, null=True)
    fielder = models.CharField(max_length=60, null=True)
    objects = CopyManager()

    def __str__(self):
        return f'{self.match_id}, {self.batting_team} vs {self.bowling_team}, {self.over}.{self.ball}'



# Match.objects.values('season').annotate(Count('id'))
# Match.objects.values('season', 'winner').annotate(Count('id')).order_by('-season')

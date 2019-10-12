from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from iplstats.models import Match, Delivery

def get_match(request, id):
    match = Match.objects.get(id=id)
    data = {
        'response': {
            "id":match.id,
            "season":match.season,
            "city":match.city,
            "date":match.date,
            "team1":match.team1,
            "team2":match.team2,
            "toss_winner":match.toss_winner,
            "toss_decision":match.toss_decision,
            "result":match.result,
            "dl_applied":match.dl_applied,
            "winner":match.winner,
            "win_by_runs":match.win_by_runs,
            "win_by_wickets":match.win_by_wickets,
            "player_of_match":match.player_of_match,
            "venue":match.venue,
            "umpire1":match.umpire1,
            "umpire2":match.umpire2,
            "umpire3":match.umpire3,
        }
    }
    return JsonResponse(data)

def get_delivery(request, id):
    delivery = Delivery.objects.get(pk=id)
    data = {
        'response':{
            'id':id,
            'match_id':delivery.match_id.id,
            'inning':delivery.inning,
            'batting_team':delivery.batting_team,
            'bowling_team':delivery.bowling_team,
            'over':delivery.over,
            'ball':delivery.ball,
            'batsman':delivery.batsman,
            'non_striker':delivery.non_striker,
            'bowler':delivery.bowler,
            'is_super_over':delivery.is_super_over,
            'wide_runs':delivery.wide_runs,
            'bye_runs':delivery.bye_runs,
            'legbye_runs':delivery.legbye_runs,
            'noball_runs':delivery.noball_runs,
            'penalty_runs':delivery.penalty_runs,
            'batsman_runs':delivery.batsman_runs,
            'extra_runs':delivery.extra_runs,
            'total_runs':delivery.total_runs,
            'player_dismissed':delivery.player_dismissed,'dismissal_kind':delivery.dismissal_kind,
            'fielder':delivery.fielder
        }
    }
    return JsonResponse(data)

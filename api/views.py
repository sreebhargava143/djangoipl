from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from iplstats.models import Match, Delivery
from django.views.decorators.csrf import csrf_exempt
from .validators import *

def get_match(request, id):
    match = get_object_or_404(Match, id=id)
    if request.method == 'GET':
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
    delivery = get_object_or_404(Delivery, id=id)
    if request.method == "GET":
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

@csrf_exempt
def post_json_match(request):
    if request.method == "POST":
        match_data = load_json_or_bad_request(request)
        validate_no_id(match_data)
        match = Match(
            season=match_data.get('season'),
            city=match_data.get('city'),
            date=match_data.get('date'),
            team1=match_data.get('team1'),
            team2=match_data.get('team2'),
            toss_winner=match_data.get('toss_winner'),
            toss_decision=match_data.get('toss_decision'),
            result=match_data.get('result'),
            dl_applied=match_data.get('dl_applied'),
            winner=match_data.get('winner'),
            win_by_runs=match_data.get('win_by_runs'),
            win_by_wickets=match_data.get('win_by_wickets'),
            player_of_match=match_data.get('player_of_match'),
            venue=match_data.get('venue'),
            umpire1=match_data.get('umpire1'),
            umpire2=match_data.get('umpire2'),
            umpire3=match_data.get('umpire3')
        )
        response = save_data_or_bad_request(match, request.method)
        return JsonResponse(response)

@csrf_exempt
def post_json_delivery(request):
    if request.method == "POST":
        delivery_data = load_json_or_bad_request(request)
        validate_no_id(delivery_data)
        match = get_object_or_404(Match, id=delivery_data.get("match_id"))
        delivery = Delivery(
            match_id=match,
            inning=delivery_data.get('inning'),
            batting_team=delivery_data.get('batting_team'),
            bowling_team=delivery_data.get('bowling_team'),
            over=delivery_data.get('over'),
            ball=delivery_data.get('ball'),
            batsman=delivery_data.get('batsman'),
            non_striker=delivery_data.get('non_striker'),
            bowler=delivery_data.get('bowler'),
            is_super_over=delivery_data.get('is_super_over'),
            wide_runs=delivery_data.get('wide_runs'),
            bye_runs=delivery_data.get('bye_runs'),
            legbye_runs=delivery_data.get('legbye_runs'),
            noball_runs=delivery_data.get('noball_runs'),
            penalty_runs=delivery_data.get('penalty_runs'),
            batsman_runs=delivery_data.get('batsman_runs'),
            extra_runs=delivery_data.get('extra_runs'),
            total_runs=delivery_data.get('total_runs'),
            player_dismissed=delivery_data.get('player_dismissed'),dismissal_kind=delivery_data.get('dismissal_kind'),
            fielder=delivery_data.get('fielder')
        )
        response = save_data_or_bad_request(delivery, request.method)
        return JsonResponse(response)

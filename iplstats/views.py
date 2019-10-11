from django.shortcuts import render
from .models import Match, Delivery
from django.db.models import Count, Sum, FloatField, Case, When
from django.db.models.functions import Cast
# Create your views here.

def home(request):
    return render(request, 'iplstats/home.html')

def matches_per_season(request):
    data = Match.objects.values('season').annotate(Count('id')).order_by('season')
    context = {
        'data':data,
        'title':'matches per season',
        'legend':'Matches Per Season',
    }
    return render(request, 'iplstats/matches_played.html', context)

def matches_won(request):
    data = Match.objects.values('season', 'winner').annotate(Count('id')).order_by('-season')
    context = context = {
        'data':data,
        'title':'matches won',
        'legend':'Matches Won By Each Team',
    }
    return render(request, 'iplstats/matches_won.html', context)

def runs_conceded(request):
    data = Match.objects.filter(season=2016).values('delivery__bowling_team').annotate(Sum('delivery__extra_runs'))
    context = {
        'data':data,
        'title':'Runs Concede',
        'legend':'Extra Runs Conceded By Each Team',
        'season':2016
    }
    return render(request, 'iplstats/runs_conceded.html', context)

def bowlers_economy(request):
    data = Match.objects.filter(season=2015).values('delivery__bowler').annotate(economy=Cast(Cast((Sum('delivery__total_runs')-Sum('delivery__bye_runs')-Sum('delivery__legbye_runs')) * 6, FloatField()) / Sum(Case(When(delivery__wide_runs=0, delivery__noball_runs=0, then=1)), default=0, output_field=FloatField()), FloatField())).order_by('economy')
    context = {
        'data':data,
        'title':'Bowlers Economy',
        'legend':'Bowlers Economy For',
        'season':2015
    }
    return render(request, 'iplstats/bowlers_economy.html', context)
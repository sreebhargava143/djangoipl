from django.shortcuts import render
from .models import Match, Delivery
from django.db.models import Count, Sum, FloatField, Case, When
from django.db.models.functions import Cast
from django.views.decorators.cache import cache_page
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)


def home(request):
    return render(request, 'iplstats/home.html')

@cache_page(CACHE_TTL)
def matches_per_season(request):
    data = Match.objects.values('season').annotate(Count('id')).order_by('season')
    context = {
        'data':data,
        'title':'matches per season',
        'legend':'Matches Per Season',
    }
    return render(request, 'iplstats/matches_played.html', context)

@cache_page(CACHE_TTL)
def matches_won(request):
    data = Match.objects.values('season', 'winner').annotate(Count('id')).order_by('season')
    context = context = {
        'data':data,
        'title':'matches won',
        'legend':'Matches Won By Each Team',
    }
    return render(request, 'iplstats/matches_won.html', context)
@cache_page(CACHE_TTL)
def runs_conceded(request):
    data = Match.objects.filter(season=2016).values('delivery__bowling_team').annotate(Sum('delivery__extra_runs')).order_by('-delivery__extra_runs__sum')
    context = {
        'data':data,
        'title':'Runs Concede',
        'legend':'Extra Runs Conceded By Each Team',
        'season':2016
    }
    return render(request, 'iplstats/runs_conceded.html', context)
@cache_page(CACHE_TTL)
def bowlers_economy(request):
    data = Match.objects.filter(season=2015).values('delivery__bowler').annotate(economy=Cast(Cast((Sum('delivery__total_runs')-Sum('delivery__bye_runs')-Sum('delivery__legbye_runs')) * 6, FloatField()) / Sum(Case(When(delivery__wide_runs=0, delivery__noball_runs=0, then=1)), default=0, output_field=FloatField()), FloatField())).order_by('economy')[:10]
    context = {
        'data':data,
        'title':'Bowlers Economy',
        'legend':'Bowlers Economy For',
        'season':2015
    }
    return render(request, 'iplstats/bowlers_economy.html', context)
@cache_page(CACHE_TTL)
def batsmen_performance(request):
    data = Match.objects.values('season', 'delivery__batsman').annotate(strike_rate=(Cast(Cast(Sum('delivery__batsman_runs')*100, FloatField()) / Sum(Case(When(delivery__wide_runs=0, delivery__noball_runs=0, then=1)),default=0, output_field=FloatField()), FloatField()))).order_by('-strike_rate')[:10]

    context = {
        'data':data,
        'title':'Batsmen Performance',
        'legend':'Batsmen Performance',
    }
    return render(request, 'iplstats/batsmen_performance.html', context)
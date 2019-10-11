from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="ipl_stats_home"),
    path('/matches_per_season', views.matches_per_season, name="ipl_stats_matches_per_season"),
    path('/matches_won', views.matches_won, name="ipl_stats_matches_won"),
    path('/runs_conceded', views.runs_conceded, name="ipl_stats_runs_conceded"),
    path('/bowlers_economy', views.bowlers_economy, name="ipl_stats_bowlers_economy"),
]

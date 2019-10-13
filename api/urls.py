from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("matches/<int:id>", views.match_rud, name="api_get_match"),
    path('deliveries/<int:id>', views.delivery_rud, name="api_get_delivery"),
    path("matches/", views.match_cr, name="api_post_json_match"),
    path("deliveries/", views.delivery_cr, name="api_post_json_delivery"),
]
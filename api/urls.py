from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("matches/<int:id>", views.get_match, name="api_get_match"),
    path('deliveries/<int:id>', views.get_delivery, name="api_get_delivery"),
    path("matches/", views.post_json_match, name="api_post_json_match"),
    path("deliveries/", views.post_json_delivery, name="api_post_json_delivery"),
]
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("matches/<int:id>", views.get_match, name="api_get_match"),
    path('deliveries/<int:id>', views.get_delivery, name="api_get_delivery")
]
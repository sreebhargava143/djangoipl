from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from iplstats.models import Match, Delivery
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict
from .validators import *

@csrf_exempt
def get_match(request, id):
    if request.method == 'GET':
        match = get_object_or_404(Match, id=id)
        response = {
            'response': model_to_dict(match)
        }
    elif request.method == "PUT":
        match = Match.objects.filter(id=id)
        match_data = load_json_or_bad_request(request)
        resoponse = update_or_bad_request(match, match_data, request)
    else:
        response = {
            'response':{
                'status':'FAILED',
                'ERROR':'METHOD NOT SUPPORTED'
            }
        }
    return JsonResponse(response)

@csrf_exempt
def get_delivery(request, id):
    if request.method == "GET":
        delivery = get_object_or_404(Delivery, id=id)
        response = {
            'response':model_to_dict(delivery)
        }
    elif request.method == "PUT":
        delivery = Delivery.objects.filter(id=id)
        delivery_data = load_json_or_bad_request(request)
        match = get_object_or_404(Match, id=delivery_data.get("match_id"))
        delivery_data['match_id'] = match
        response = update_or_bad_request(delivery, delivery_data, request)
    else:
        response = {
            'response':{
                'status':'FAILED',
                'ERROR':'METHOD NOT SUPPORTED'
            }
        }
    return JsonResponse(response)

@csrf_exempt
def post_json_match(request):
    if request.method == "POST":
        match_data = load_json_or_bad_request(request)
        validate_no_id(match_data)
        match = Match(**match_data)
        response = save_or_bad_request(match, request)
        return JsonResponse(response)

@csrf_exempt
def post_json_delivery(request):
    if request.method == "POST":
        delivery_data = load_json_or_bad_request(request)
        validate_no_id(delivery_data)
        match = get_object_or_404(Match, id=delivery_data.get("match_id"))
        delivery_data['match_id'] = match
        delivery = Delivery(**delivery_data)
        response = save_or_bad_request(delivery, request)
        return JsonResponse(response)

from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from iplstats.models import Match, Delivery
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict
from .validators import *

@csrf_exempt
def get_match(request, id):
    match = get_object_or_bad_request(Match, id)
    if request.method == 'GET':
        match = match.first()
        response = {
            'response': model_to_dict(match)
        }
    elif request.method == "PUT":
        match_data = load_json_or_bad_request(request)
        validate_no_id(match_data)
        response = update_or_bad_request(match, match_data, request)
    elif request.method == "DELETE":
        response = delete_or_bad_request(match, request)
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
    delivery = get_object_or_bad_request(Delivery, id)
    if request.method == "GET":
        delivery = delivery.first()
        response = {
            'response':model_to_dict(delivery)
        }
    elif request.method == "PUT":
        delivery_data = load_json_or_bad_request(request)
        if 'match_id' in delivery_data:
            match = get_object_or_bad_request(Match, id=delivery_data.get("match_id")).first()
            delivery_data['match_id'] = match
        response = update_or_bad_request(delivery, delivery_data, request)
    elif request.method == "DELETE":
        response = delete_or_bad_request(delivery, request)
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

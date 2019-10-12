import json
from iplstats.models import Match, Delivery
from django.core.exceptions import ValidationError, SuspiciousOperation

def load_json_or_bad_request(request):
    try:
        data = json.loads(request.body)
    except ValueError:
        data = {}
        raise SuspiciousOperation("INVALID JSON !")
        
    return data
    
def save_data_or_bad_request(data, method):
    try:
        data.save()
        response_data = {
            'response':{
                'status':'SUCCESS',
                'method':method
            }
        }
    except Exception:
        response_data = {
            'response':{
                'status':'FAILED',
            }
        }
        raise SuspiciousOperation("INVALID DATA !")
    return response_data

def validate_no_id(data):
    if data.get("id"):
        raise ValidationError("VIOLATES 'AUTO ID' !")

def validate_foreign_key(delivery):
    try:
        match = Match.objects.get(id=delivery.get('match_id'))
    except Exception as e:
        match = None
        raise ValidationError("VIOLATES FOREIGN KEY CONSTRAINT !")
    return match

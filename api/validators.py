import json
from iplstats.models import Match, Delivery
from django.core.exceptions import ValidationError, SuspiciousOperation
from django.db import transaction

def load_json_or_bad_request(request):
    try:
        data = json.loads(request.body)
    except ValueError:
        data = {}
        raise SuspiciousOperation("INVALID JSON !")
        
    return data

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

@transaction.atomic
def save_or_bad_request(db_object, request):
    try:
        print(db_object)
        print(db_object.save())
        response_data = {
            'response':{
                'status':'SUCCESS',
                'method':request.method,
                'action':'NEW RECORD CREATED'
            }
        }
    except Exception:
        response_data = {
            'response':{
                'status':'FAILED',
                'method':request.method,
                'action':'NO ACTION'
            }
        }
        raise SuspiciousOperation("INVALID DATA !")
    return response_data

@transaction.atomic
def update_or_bad_request(db_object, data, request):
    try:
        db_object.update(**data)
        response_data = {
            'response':{
                'status':'SUCCESS',
                'method':request.method,
                'action':'RECORD UPDATED'
            }
        }
    except Exception as e:
        response_data = {
            'response':{
                'status':'FAILED',
                'method':request.method,
                'action':'NO ACTION'
            }
        }
        raise SuspiciousOperation("INVALID DATA !", e)
    return response_data

@transaction.atomic
def delete_or_bad_request(db_object, request):
    db_object.delete()
    response_data = {
            'response':{
                'status':'SUCCESS',
                'method':request.method,
                'action':'RECORD DELETED'
            }
        }
    return response_data


def get_object_or_bad_request(Model, id):
    db_object = Model.objects.filter(id=id)
    print(db_object)
    if db_object.first() is None:
        print("Entered if")
        raise SuspiciousOperation("INVALID ID !")
    
    return db_object
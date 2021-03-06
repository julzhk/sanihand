from django.shortcuts import render, HttpResponse
import json
import logging
from django.http import HttpResponse
from django.db.models.loading import get_model
from django.core.exceptions import FieldError, ObjectDoesNotExist
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.decorators.csrf import csrf_exempt
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
from models import Beacon, User
from collections import defaultdict


def home(request):
    return HttpResponse('hi')

def dashboard(request):
    '''
     give overview of who's doing well
    '''
    all_users = User.objects.all()
    t = get_template('tracking/dashboard.html')
    html = t.render(Context({
        'users':all_users,
        'name_count': len(all_users),
        'half_count': len(all_users)/2 + 1
    }))
    return HttpResponse(html)

def report(request):
    '''
     give overview of who's doing well as a team oriented list
    '''
    all_users = User.objects.all().order_by('dept')

    t = get_template('tracking/report.html')
    html = t.render(Context({'users':all_users,
                              }))
    return HttpResponse(html)



def get_beacon(request, beaconid=None):
    if beaconid == '':
        beacons = Beacon.objects.all()
        data = [beacon.to_dict() for beacon in beacons]
    else:
        try:
            beacon = Beacon.objects.get(beacon_id=beaconid)
            data = beacon.to_dict()
        except Beacon.DoesNotExist:
            data = {}
    response = HttpResponse(json.dumps(data) , content_type="application/json")
    response['Access-Control-Allow-Origin'] = '*'
    return response


@csrf_exempt
def checkin_beacon(request):
    data =  json.loads(request.body)
    # user, clean_count, dirty_count
    user, usercreated = User.objects.get_or_create(name=data['user'] or 'anon')
    user.clean_count = int(data['clean_count']) or 0
    user.dirty_count = int(data['dirty_count']) or 0
    user.save()
    beacon, beaconcreated = Beacon.objects.get_or_create(
            beacon_id=data['beacon_id']
    )
    if beaconcreated:
        beacon.name = 'beacon no %s ' % beacon.id
        beacon.save()
    return HttpResponse(str(data))

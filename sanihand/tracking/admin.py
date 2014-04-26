from django.contrib import admin
from tracking.models import Beacon, BeaconCheckin
admin.site.register(BeaconCheckin)
admin.site.register(Beacon)
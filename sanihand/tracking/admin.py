from django.contrib import admin
import tracking.models
from tracking.models import Beacon, BeaconCheckin
admin.site.register(BeaconCheckin)
admin.site.register(Beacon)
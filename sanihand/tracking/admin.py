from django.contrib import admin
from sanihand.tracking.models import Beacon, BeaconCheckin
admin.site.register(BeaconCheckin)
admin.site.register(Beacon)
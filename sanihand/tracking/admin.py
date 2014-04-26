from django.contrib import admin
from sanihand.tracking.models import Beacon, BeaconCheckin, User
admin.site.register(BeaconCheckin)
admin.site.register(Beacon)
admin.site.register(User)
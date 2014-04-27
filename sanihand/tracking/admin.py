from django.contrib import admin
from sanihand.tracking.models import Beacon, User

class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'dept','clean_count','dirty_count')

class BeaconAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_clean','beacon_id')
    list_filter = ('is_clean', )

admin.site.register(Beacon,BeaconAdmin)
admin.site.register(User, UserAdmin)


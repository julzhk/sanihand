from django.db import models
from datetime import datetime

class Beacon(models.Model):
    name = models.TextField()
    is_clean = models.BooleanField(default=True)
    beacon_id = models.TextField()

    def __str__(self):
        return '%s id:%s' % (self.name, self.beacon_id)
B
class BeaconCheckin(models.Model):
    date = models.DateTimeField(auto_now_add=True, blank=True)
    user = models.TextField()
    user_id = models.TextField()
    beacon= models.ForeignKey(Beacon)


    def __str__(self):
        return 'checkin id %s ' % (self.id or '-')


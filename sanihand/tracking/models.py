from django.db import models
from datetime import datetime

class User(models.Model):
    name = models.TextField()

    def __str__(self):
        return '%s id:%s' % (self.name, self.id)


class Beacon(models.Model):
    name = models.TextField()
    is_clean = models.BooleanField(default=True)
    beacon_id = models.TextField()

    def __str__(self):
        return '%s id:%s' % (self.name, self.beacon_id)

    def to_dict(self):
        self_dict = self.__dict__
        r = {k: self_dict[k] for k in self_dict if k[0] != '_'}
        return r

class BeaconCheckin(models.Model):
    date = models.DateTimeField(auto_now_add=True, blank=True)
    # user = models.ForeignKey(User)
    beacon= models.ForeignKey(Beacon)

    def __str__(self):
        return 'checkin id %s ' % (self.id or '-')

    def user_scores(self):
        return 0


from django.test import TestCase
from models import Beacon, BeaconCheckin, User
from django.test import TestCase


class ReportScore(TestCase):
    def setUp(self):
        self.cleanbeacon = Beacon(name='sink',
                             is_clean = True,
                             beacon_id='123'
                             )
        self.cleanbeacon.save()
        self.dirtybeacon= Beacon(name='door',
                             is_clean = False,
                             beacon_id='345'
                             )
        self.dirtybeacon.save()

    def test_simple(self):
        check1 = BeaconCheckin(user='julz',beacon=self.cleanbeacon)
        check1.save()
        testuser = User.objects.get(name='julz')
        self.assertEqual(testuser.name, 'julz')


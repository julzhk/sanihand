# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'BeaconCheckin.user'
        db.add_column(u'tracking_beaconcheckin', 'user',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=0, to=orm['tracking.User']),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'BeaconCheckin.user'
        db.delete_column(u'tracking_beaconcheckin', 'user_id')


    models = {
        u'tracking.beacon': {
            'Meta': {'object_name': 'Beacon'},
            'beacon_id': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_clean': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {})
        },
        u'tracking.beaconcheckin': {
            'Meta': {'object_name': 'BeaconCheckin'},
            'beacon': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tracking.Beacon']"}),
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tracking.User']"})
        },
        u'tracking.user': {
            'Meta': {'object_name': 'User'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['tracking']
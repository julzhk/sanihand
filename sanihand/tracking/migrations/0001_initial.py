# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Beacon'
        db.create_table(u'tracking_beacon', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.TextField')()),
            ('is_clean', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('beacon_id', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'tracking', ['Beacon'])

        # Adding model 'BeaconCheckin'
        db.create_table(u'tracking_beaconcheckin', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('user', self.gf('django.db.models.fields.TextField')()),
            ('user_id', self.gf('django.db.models.fields.TextField')()),
            ('beacon', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['tracking.Beacon'])),
        ))
        db.send_create_signal(u'tracking', ['BeaconCheckin'])


    def backwards(self, orm):
        # Deleting model 'Beacon'
        db.delete_table(u'tracking_beacon')

        # Deleting model 'BeaconCheckin'
        db.delete_table(u'tracking_beaconcheckin')


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
            'user': ('django.db.models.fields.TextField', [], {}),
            'user_id': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['tracking']
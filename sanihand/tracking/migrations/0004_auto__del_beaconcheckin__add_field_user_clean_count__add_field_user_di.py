# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'BeaconCheckin'
        db.delete_table(u'tracking_beaconcheckin')

        # Adding field 'User.clean_count'
        db.add_column(u'tracking_user', 'clean_count',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'User.dirty_count'
        db.add_column(u'tracking_user', 'dirty_count',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)


    def backwards(self, orm):
        # Adding model 'BeaconCheckin'
        db.create_table(u'tracking_beaconcheckin', (
            ('date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('beacon', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['tracking.Beacon'])),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['tracking.User'])),
        ))
        db.send_create_signal(u'tracking', ['BeaconCheckin'])

        # Deleting field 'User.clean_count'
        db.delete_column(u'tracking_user', 'clean_count')

        # Deleting field 'User.dirty_count'
        db.delete_column(u'tracking_user', 'dirty_count')


    models = {
        u'tracking.beacon': {
            'Meta': {'object_name': 'Beacon'},
            'beacon_id': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_clean': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {})
        },
        u'tracking.user': {
            'Meta': {'object_name': 'User'},
            'clean_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'dirty_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['tracking']
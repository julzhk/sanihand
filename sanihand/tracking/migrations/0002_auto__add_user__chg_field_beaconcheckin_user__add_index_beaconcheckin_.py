# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'User'
        db.create_table(u'tracking_user', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'tracking', ['User'])


        # Renaming column for 'BeaconCheckin.user' to match new field type.
        db.rename_column(u'tracking_beaconcheckin', 'user', 'user_id')
        # Changing field 'BeaconCheckin.user'
        db.alter_column(u'tracking_beaconcheckin', 'user_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['tracking.User']))
        # Adding index on 'BeaconCheckin', fields ['user']
        db.create_index(u'tracking_beaconcheckin', ['user_id'])


    def backwards(self, orm):
        # Removing index on 'BeaconCheckin', fields ['user']
        db.delete_index(u'tracking_beaconcheckin', ['user_id'])

        # Deleting model 'User'
        db.delete_table(u'tracking_user')


        # Renaming column for 'BeaconCheckin.user' to match new field type.
        db.rename_column(u'tracking_beaconcheckin', 'user_id', 'user')
        # Changing field 'BeaconCheckin.user'
        db.alter_column(u'tracking_beaconcheckin', 'user', self.gf('django.db.models.fields.TextField')())

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
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tracking.User']"}),
            'user_id': ('django.db.models.fields.TextField', [], {})
        },
        u'tracking.user': {
            'Meta': {'object_name': 'User'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['tracking']
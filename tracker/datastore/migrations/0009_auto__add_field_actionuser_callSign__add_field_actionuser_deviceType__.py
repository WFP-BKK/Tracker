# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'ActionUser.callSign'
        db.add_column(u'users', 'callSign',
                      self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True),
                      keep_default=False)

        # Adding field 'ActionUser.deviceType'
        db.add_column(u'users', 'deviceType',
                      self.gf('django.db.models.fields.CharField')(max_length=40, null=True, blank=True),
                      keep_default=False)

        # Adding field 'ActionUser.deviceModel'
        db.add_column(u'users', 'deviceModel',
                      self.gf('django.db.models.fields.CharField')(max_length=40, null=True, blank=True),
                      keep_default=False)

        # Adding field 'ActionUser.radioServer'
        db.add_column(u'users', 'radioServer',
                      self.gf('django.db.models.fields.CharField')(max_length=40, null=True, blank=True),
                      keep_default=False)

        # Adding field 'ActionUser.firstName'
        db.add_column(u'users', 'firstName',
                      self.gf('django.db.models.fields.CharField')(max_length=40, null=True, blank=True),
                      keep_default=False)

        # Adding field 'ActionUser.lastName'
        db.add_column(u'users', 'lastName',
                      self.gf('django.db.models.fields.CharField')(max_length=40, null=True, blank=True),
                      keep_default=False)

        # Adding field 'ActionUser.organization'
        db.add_column(u'users', 'organization',
                      self.gf('django.db.models.fields.CharField')(max_length=40, null=True, blank=True),
                      keep_default=False)

        # Adding field 'ActionUser.epicNumber'
        db.add_column(u'users', 'epicNumber',
                      self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True),
                      keep_default=False)

        # Adding field 'ActionUser.inactiveUser'
        db.add_column(u'users', 'inactiveUser',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'ActionUser.sipAddress'
        db.add_column(u'users', 'sipAddress',
                      self.gf('django.db.models.fields.CharField')(max_length=80, null=True, blank=True),
                      keep_default=False)

        # Adding field 'ActionUser.emailAddress'
        db.add_column(u'users', 'emailAddress',
                      self.gf('django.db.models.fields.EmailField')(max_length=75, null=True, blank=True),
                      keep_default=False)

        # Adding field 'ActionUser.timeZone'
        db.add_column(u'users', 'timeZone',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'ActionUser.callSign'
        db.delete_column(u'users', 'callSign')

        # Deleting field 'ActionUser.deviceType'
        db.delete_column(u'users', 'deviceType')

        # Deleting field 'ActionUser.deviceModel'
        db.delete_column(u'users', 'deviceModel')

        # Deleting field 'ActionUser.radioServer'
        db.delete_column(u'users', 'radioServer')

        # Deleting field 'ActionUser.firstName'
        db.delete_column(u'users', 'firstName')

        # Deleting field 'ActionUser.lastName'
        db.delete_column(u'users', 'lastName')

        # Deleting field 'ActionUser.organization'
        db.delete_column(u'users', 'organization')

        # Deleting field 'ActionUser.epicNumber'
        db.delete_column(u'users', 'epicNumber')

        # Deleting field 'ActionUser.inactiveUser'
        db.delete_column(u'users', 'inactiveUser')

        # Deleting field 'ActionUser.sipAddress'
        db.delete_column(u'users', 'sipAddress')

        # Deleting field 'ActionUser.emailAddress'
        db.delete_column(u'users', 'emailAddress')

        # Deleting field 'ActionUser.timeZone'
        db.delete_column(u'users', 'timeZone')


    models = {
        u'datastore.actionuser': {
            'Meta': {'object_name': 'ActionUser', 'db_table': "u'users'"},
            'callSign': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'deviceModel': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'deviceType': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'emailAddress': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'epicNumber': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'firstName': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inactiveUser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'lastName': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'organization': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'radioServer': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'sipAddress': ('django.db.models.fields.CharField', [], {'max_length': '80', 'null': 'True', 'blank': 'True'}),
            'timeZone': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '60'})
        },
        u'datastore.currentposition': {
            'Meta': {'object_name': 'CurrentPosition'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'position': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['datastore.Position']"}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['datastore.ActionUser']", 'unique': 'True'})
        },
        u'datastore.geofence': {
            'Meta': {'object_name': 'GeoFence'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'fence': ('django.contrib.gis.db.models.fields.PolygonField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'warningIn': ('django.db.models.fields.CharField', [], {'max_length': '144', 'null': 'True', 'blank': 'True'}),
            'warningOut': ('django.db.models.fields.CharField', [], {'max_length': '144', 'null': 'True', 'blank': 'True'})
        },
        u'datastore.icon': {
            'Meta': {'object_name': 'Icon', 'db_table': "u'icons'"},
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "'ID'"}),
            'name': ('django.db.models.fields.TextField', [], {'max_length': '765', 'db_column': "'Name'"}),
            'url': ('django.db.models.fields.TextField', [], {'max_length': '1536', 'db_column': "'URL'"})
        },
        u'datastore.incident': {
            'Meta': {'object_name': 'Incident'},
            'actionDate': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'date_reported': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'image_ref': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'location': ('django.contrib.gis.db.models.fields.PointField', [], {'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['datastore.ActionUser']"})
        },
        u'datastore.logginglist': {
            'Meta': {'object_name': 'LoggingList'},
            'actionDate': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'errorText': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'reportingServer': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'})
        },
        u'datastore.position': {
            'Meta': {'object_name': 'Position', 'db_table': "u'positions'"},
            'altitude': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "'Altitude'", 'blank': 'True'}),
            'angle': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "'Angle'", 'blank': 'True'}),
            'batterystatus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "'BatteryStatus'", 'blank': 'True'}),
            'comments': ('django.db.models.fields.TextField', [], {'max_length': '765', 'null': 'True', 'db_column': "'Comments'", 'blank': 'True'}),
            'dateadded': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'db_column': "'DateAdded'", 'blank': 'True'}),
            'dateoccurred': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'db_column': "'DateOccurred'", 'blank': 'True'}),
            'icon': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['datastore.Icon']", 'null': 'True', 'db_column': "'FK_Icons_ID'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imageurl': ('django.db.models.fields.files.ImageField', [], {'max_length': '765', 'null': 'True', 'db_column': "'ImageURL'", 'blank': 'True'}),
            'location': ('django.contrib.gis.db.models.fields.PointField', [], {'null': 'True', 'blank': 'True'}),
            'signalstrength': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "'SignalStrength'", 'blank': 'True'}),
            'signalstrengthmax': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "'SignalStrengthMax'", 'blank': 'True'}),
            'signalstrengthmin': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "'SignalStrengthMin'", 'blank': 'True'}),
            'speed': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "'Speed'", 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['datastore.ActionUser']", 'db_column': "'FK_Users_ID'"})
        },
        u'datastore.radioserver': {
            'Meta': {'object_name': 'RadioServer'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latestCheck': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'latestUpdate': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'refreshPeriod': ('django.db.models.fields.IntegerField', [], {'default': '300'}),
            'serverEnabled': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'serverName': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'datastore.trip': {
            'Meta': {'object_name': 'Trip', 'db_table': "u'trips'"},
            'comments': ('django.db.models.fields.TextField', [], {'max_length': '1024', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['datastore.ActionUser']", 'db_column': "'FK_Users_ID'"})
        },
        u'datastore.userdetail': {
            'Meta': {'object_name': 'UserDetail'},
            'callSign': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'deviceModel': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'deviceType': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'emailAddress': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'epicNumber': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'firstName': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inactiveUser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'lastName': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'organization': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'radioServer': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'sipAddress': ('django.db.models.fields.CharField', [], {'max_length': '80', 'null': 'True', 'blank': 'True'}),
            'timeZone': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['datastore.ActionUser']", 'unique': 'True'})
        }
    }

    complete_apps = ['datastore']
# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'RemoteStation'
        db.delete_table(u'datastore_remotestation')

        # Deleting model 'ContactWays'
        db.delete_table(u'datastore_contactways')

        # Adding model 'GeoFence'
        db.create_table(u'datastore_geofence', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('warningIn', self.gf('django.db.models.fields.CharField')(max_length=144, null=True, blank=True)),
            ('warningOut', self.gf('django.db.models.fields.CharField')(max_length=144, null=True, blank=True)),
            ('fence', self.gf('django.contrib.gis.db.models.fields.PolygonField')()),
        ))
        db.send_create_signal(u'datastore', ['GeoFence'])

        # Adding model 'RadioServer'
        db.create_table(u'datastore_radioserver', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('serverName', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('latestUpdate', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('serverEnabled', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('refreshPeriod', self.gf('django.db.models.fields.IntegerField')(default=300)),
            ('latestCheck', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'datastore', ['RadioServer'])

        # Adding model 'Incident'
        db.create_table(u'datastore_incident', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['datastore.ActionUser'])),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('location', self.gf('django.contrib.gis.db.models.fields.PointField')(null=True, blank=True)),
            ('date_reported', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('actionDate', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, null=True, blank=True)),
            ('image_ref',self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
        ))
        db.send_create_signal(u'datastore', ['Incident'])


        # Changing field 'Trip.comments'
        db.alter_column(u'trips', 'comments', self.gf('django.db.models.fields.TextField')(max_length=1024, null=True))

        # Adding field 'Position.location'
        
        db.add_column(u'positions', 'location',
                      self.gf('django.contrib.gis.db.models.fields.PointField')(null=True, blank=True),
                      keep_default=False)



        # Changing field 'Icon.url'
        db.alter_column(u'icons', 'URL', self.gf('django.db.models.fields.TextField')(max_length=1536, db_column='URL'))

        # Changing field 'Icon.name'
        db.alter_column(u'icons', 'Name', self.gf('django.db.models.fields.TextField')(max_length=765, db_column='Name'))

    def backwards(self, orm):
        # Adding model 'RemoteStation'
        db.create_table(u'datastore_remotestation', (
            ('reportingFrequency', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('reportingServer', self.gf('django.db.models.fields.CharField')(max_length=20, primary_key=True)),
            ('lastReported', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, null=True, blank=True)),
        ))
        db.send_create_signal('datastore', ['RemoteStation'])

        # Adding model 'ContactWays'
        db.create_table(u'datastore_contactways', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('contactString', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('actionUser', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['datastore.ActionUser'])),
            ('contactProtocol', self.gf('django.db.models.fields.CharField')(max_length=10)),
        ))
        db.send_create_signal('datastore', ['ContactWays'])

        # Deleting model 'GeoFence'
        db.delete_table(u'datastore_geofence')

        # Deleting model 'RadioServer'
        db.delete_table(u'datastore_radioserver')

        # Deleting model 'Incident'
        db.delete_table(u'datastore_incident')


        # Changing field 'Trip.comments'
        db.alter_column(u'trips', 'comments', self.gf('django.db.models.fields.CharField')(max_length=1024, null=True))
        # Deleting field 'Position.location'
        db.delete_column(u'positions', 'location')



        # Changing field 'Icon.url'
        db.alter_column(u'icons', 'URL', self.gf('django.db.models.fields.CharField')(max_length=1536, db_column='URL'))

        # Changing field 'Icon.name'
        db.alter_column(u'icons', 'Name', self.gf('django.db.models.fields.CharField')(max_length=765, db_column='Name'))

    models = {
        u'datastore.actionuser': {
            'Meta': {'object_name': 'ActionUser', 'db_table': "u'users'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
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
            'latitude': ('django.db.models.fields.FloatField', [], {'db_column': "'Latitude'"}),
            'longitude': ('django.db.models.fields.FloatField', [], {'db_column': "'Longitude'"}),
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
            'sipAddress': ('django.db.models.fields.CharField', [], {'max_length': '80', 'null': 'True', 'blank': 'True'}),
            'timeZone': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['datastore.ActionUser']", 'unique': 'True'})
        }
    }

    complete_apps = ['datastore']
# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Icon'
        db.create_table(u'icons', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column='ID')),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=765, db_column='Name')),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=1536, db_column='URL')),
        ))
        db.send_create_signal('datastore', ['Icon'])

        # Adding model 'ActionUser'
        db.create_table(u'users', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('username', self.gf('django.db.models.fields.CharField')(unique=True, max_length=60)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True)),
        ))
        db.send_create_signal('datastore', ['ActionUser'])

        # Adding model 'UserDetail'
        db.create_table('datastore_userdetail', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['datastore.ActionUser'], unique=True)),
            ('callSign', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('deviceType', self.gf('django.db.models.fields.CharField')(max_length=40, null=True, blank=True)),
            ('deviceModel', self.gf('django.db.models.fields.CharField')(max_length=40, null=True, blank=True)),
            ('firstName', self.gf('django.db.models.fields.CharField')(max_length=40, null=True, blank=True)),
            ('lastName', self.gf('django.db.models.fields.CharField')(max_length=40, null=True, blank=True)),
            ('organization', self.gf('django.db.models.fields.CharField')(max_length=40, null=True, blank=True)),
            ('epicNumber', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
            ('inactiveUser', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('sipAddress', self.gf('django.db.models.fields.CharField')(max_length=80, null=True, blank=True)),
            ('emailAddress', self.gf('django.db.models.fields.EmailField')(max_length=75, null=True, blank=True)),
            ('timeZone', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal('datastore', ['UserDetail'])

        # Adding model 'Position'
        db.create_table(u'positions', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['datastore.ActionUser'], db_column='FK_Users_ID')),
            ('icon', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['datastore.Icon'], null=True, db_column='FK_Icons_ID', blank=True)),
            ('latitude', self.gf('django.db.models.fields.FloatField')(db_column='Latitude')),
            ('longitude', self.gf('django.db.models.fields.FloatField')(db_column='Longitude')),
            ('altitude', self.gf('django.db.models.fields.FloatField')(null=True, db_column='Altitude', blank=True)),
            ('speed', self.gf('django.db.models.fields.FloatField')(null=True, db_column='Speed', blank=True)),
            ('angle', self.gf('django.db.models.fields.FloatField')(null=True, db_column='Angle', blank=True)),
            ('dateadded', self.gf('django.db.models.fields.DateTimeField')(null=True, db_column='DateAdded', blank=True)),
            ('dateoccurred', self.gf('django.db.models.fields.DateTimeField')(null=True, db_column='DateOccurred', blank=True)),
            ('comments', self.gf('django.db.models.fields.CharField')(null=True,max_length=765, db_column='Comments', blank=True)),
            ('imageurl', self.gf('django.db.models.fields.files.ImageField')(max_length=765, null=True, db_column='ImageURL', blank=True)),
            ('signalstrength', self.gf('django.db.models.fields.IntegerField')(null=True, db_column='SignalStrength', blank=True)),
            ('signalstrengthmax', self.gf('django.db.models.fields.IntegerField')(null=True, db_column='SignalStrengthMax', blank=True)),
            ('signalstrengthmin', self.gf('django.db.models.fields.IntegerField')(null=True, db_column='SignalStrengthMin', blank=True)),
            ('batterystatus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column='BatteryStatus', blank=True)),
        ))
        db.send_create_signal('datastore', ['Position'])

        # Adding model 'CurrentPosition'
        db.create_table('datastore_currentposition', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['datastore.ActionUser'], unique=True)),
            ('position', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['datastore.Position'])),
        ))
        db.send_create_signal('datastore', ['CurrentPosition'])

        # Adding model 'Trip'
        db.create_table(u'trips', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['datastore.ActionUser'], db_column='FK_Users_ID')),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('comments', self.gf('django.db.models.fields.CharField')(max_length=1024, null=True, blank=True)),
        ))
        db.send_create_signal('datastore', ['Trip'])

        # Adding model 'ContactWays'
        db.create_table('datastore_contactways', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('actionUser', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['datastore.ActionUser'])),
            ('contactProtocol', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('contactString', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal('datastore', ['ContactWays'])

        # Adding model 'LoggingList'
        db.create_table('datastore_logginglist', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('reportingServer', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('errorText', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('actionDate', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, null=True, blank=True)),
        ))
        db.send_create_signal('datastore', ['LoggingList'])

        # Adding model 'RemoteStation'
        db.create_table('datastore_remotestation', (
            ('reportingServer', self.gf('django.db.models.fields.CharField')(max_length=20, primary_key=True)),
            ('lastReported', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, null=True, blank=True)),
            ('reportingFrequency', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal('datastore', ['RemoteStation'])


    def backwards(self, orm):
        # Deleting model 'Icon'
        db.delete_table(u'icons')

        # Deleting model 'ActionUser'
        db.delete_table(u'users')

        # Deleting model 'UserDetail'
        db.delete_table('datastore_userdetail')

        # Deleting model 'Position'
        db.delete_table(u'positions')

        # Deleting model 'CurrentPosition'
        db.delete_table('datastore_currentposition')

        # Deleting model 'Trip'
        db.delete_table(u'trips')

        # Deleting model 'ContactWays'
        db.delete_table('datastore_contactways')

        # Deleting model 'LoggingList'
        db.delete_table('datastore_logginglist')

        # Deleting model 'RemoteStation'
        db.delete_table('datastore_remotestation')


    models = {
        'datastore.actionuser': {
            'Meta': {'object_name': 'ActionUser', 'db_table': "u'users'"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '60'})
        },
        'datastore.contactways': {
            'Meta': {'object_name': 'ContactWays'},
            'actionUser': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['datastore.ActionUser']"}),
            'contactProtocol': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'contactString': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'datastore.currentposition': {
            'Meta': {'object_name': 'CurrentPosition'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'position': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['datastore.Position']"}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['datastore.ActionUser']", 'unique': 'True'})
        },
        'datastore.icon': {
            'Meta': {'object_name': 'Icon', 'db_table': "u'icons'"},
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "'ID'"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '765', 'db_column': "'Name'"}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '1536', 'db_column': "'URL'"})
        },
        'datastore.logginglist': {
            'Meta': {'object_name': 'LoggingList'},
            'actionDate': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'errorText': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'reportingServer': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'})
        },
        'datastore.position': {
            'Meta': {'object_name': 'Position', 'db_table': "u'positions'"},
            'altitude': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "'Altitude'", 'blank': 'True'}),
            'angle': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "'Angle'", 'blank': 'True'}),
            'batterystatus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "'BatteryStatus'", 'blank': 'True'}),
            'comments': ('django.db.models.fields.CharField', [], {'max_length': '765', 'db_column': "'Comments'", 'blank': 'True'}),
            'dateadded': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'db_column': "'DateAdded'", 'blank': 'True'}),
            'dateoccurred': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'db_column': "'DateOccurred'", 'blank': 'True'}),
            'icon': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['datastore.Icon']", 'null': 'True', 'db_column': "'FK_Icons_ID'", 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imageurl': ('django.db.models.fields.files.ImageField', [], {'max_length': '765', 'null': 'True', 'db_column': "'ImageURL'", 'blank': 'True'}),
            'latitude': ('django.db.models.fields.FloatField', [], {'db_column': "'Latitude'"}),
            'longitude': ('django.db.models.fields.FloatField', [], {'db_column': "'Longitude'"}),
            'signalstrength': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "'SignalStrength'", 'blank': 'True'}),
            'signalstrengthmax': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "'SignalStrengthMax'", 'blank': 'True'}),
            'signalstrengthmin': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "'SignalStrengthMin'", 'blank': 'True'}),
            'speed': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "'Speed'", 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['datastore.ActionUser']", 'db_column': "'FK_Users_ID'"})
        },
        'datastore.remotestation': {
            'Meta': {'object_name': 'RemoteStation'},
            'lastReported': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'reportingFrequency': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'reportingServer': ('django.db.models.fields.CharField', [], {'max_length': '20', 'primary_key': 'True'})
        },
        'datastore.trip': {
            'Meta': {'object_name': 'Trip', 'db_table': "u'trips'"},
            'comments': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['datastore.ActionUser']", 'db_column': "'FK_Users_ID'"})
        },
        'datastore.userdetail': {
            'Meta': {'object_name': 'UserDetail'},
            'callSign': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'deviceModel': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'deviceType': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'emailAddress': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'epicNumber': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'firstName': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inactiveUser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'lastName': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'organization': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'sipAddress': ('django.db.models.fields.CharField', [], {'max_length': '80', 'null': 'True', 'blank': 'True'}),
            'timeZone': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['datastore.ActionUser']", 'unique': 'True'})
        }
    }

    complete_apps = ['datastore']
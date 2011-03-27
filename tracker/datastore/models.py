# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.

from django.db import models
from django.db.models import Max

class Icon(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') 
    name = models.CharField(max_length=765, db_column='Name') 
    url = models.CharField(max_length=1536, db_column='URL') 
    class Meta:
        db_table = u'icons'

class ActionUser(models.Model):
    username = models.CharField(unique=True, max_length=60)
    password = models.CharField(max_length=150, null=True, blank=True)
    class Meta:
        db_table = u'users'
    def __unicode__(self):
        x = self.UserDetails.firstName
        if x != '':
            return '%s' % (x)
        else:
            return '%s' % (self.username)
    
    
    def myLatestPos(self):
        #myPos = Position()
        try:
            return CurrentPosition.object.get(id=self.positions_set.aggregate(Max('id'))['id__max'])
        except:
            return

class UserDetail(models.Model):
    user = models.OneToOneField(ActionUser)
    callSign = models.CharField(max_length=20, null=True, blank=True)
    firstName = models.CharField(max_length=40, null=True, blank=True)
    lastName = models.CharField(max_length=40, null=True, blank=True)
    organization = models.CharField(max_length=40, null=True, blank=True)
    epicNumber = models.CharField(max_length=10, null=True, blank=True)
    inactiveUser = models.BooleanField(blank=True)
    
class Position(models.Model):
    user = models.ForeignKey(ActionUser, db_column='FK_Users_ID') 
    icon = models.ForeignKey(Icon, db_column='FK_Icons_ID', blank=True) 
    latitude = models.FloatField(db_column='Latitude') 
    longitude = models.FloatField(db_column='Longitude') 
    altitude = models.FloatField(null=True, db_column='Altitude', blank=True) 
    speed = models.FloatField(null=True, db_column='Speed', blank=True) 
    angle = models.FloatField(null=True, db_column='Angle', blank=True) 
    dateadded = models.DateTimeField(db_column='DateAdded') 
    dateoccurred = models.DateTimeField(null=True, db_column='DateOccurred', blank=True) 
    comments = models.CharField(max_length=765, db_column='Comments', blank=True) 
    imageurl = models.CharField(max_length=765, db_column='ImageURL', blank=True) 
    signalstrength = models.IntegerField(null=True, db_column='SignalStrength', blank=True) 
    signalstrengthmax = models.IntegerField(null=True, db_column='SignalStrengthMax', blank=True) 
    signalstrengthmin = models.IntegerField(null=True, db_column='SignalStrengthMin', blank=True) 
    batterystatus = models.IntegerField(null=True, db_column='BatteryStatus', blank=True) 
    class Meta:
        db_table = u'positions'
    def __unicode__(self):
        return '%s "%s" %s' % (self.user, self.dateoccurred,self.latitude )
        
class CurrentPosition(models.Model):
    user = models.OneToOneField(ActionUser) 
    position = models.ForeignKey(Position)
    
    
    


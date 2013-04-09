from django.contrib.gis.db import models
from django.db.models import Max


FENCE_TYPE = (
    ('DZ', 'Danger Zone'),
    ('SZ', 'Safe Zone'),
)

class Icon( models.Model ):
    id = models.IntegerField( primary_key = True, db_column = 'ID' )
    name = models.TextField( max_length = 765, db_column = 'Name' )
    url = models.TextField( max_length = 1536, db_column = 'URL' )
    class Meta:
        db_table = u'icons'

    def __unicode__(self):
        return self.name 


class ActionUser( models.Model ):
    username = models.CharField( unique = True, max_length = 60 )
    password = models.CharField( max_length = 150, null = True, blank = True )
    objects = models.GeoManager()
    class Meta:
        db_table = u'users'

    def __unicode__( self ):
        try:
            x,new_user = UserDetail.objects.get( user = self )
        except:
            x = ''
        if x != '':
            return '%s - %s' % ( x, self.username )
        else:
            return ' NA - %s' % ( self.username )

    def myLatestPos( self ):
        try:
            return CurrentPosition.object.get( id = self.positions_set.aggregate( Max( 'id' ) )['id__max'] )
        except:
            return
    def myTag (self):
        x = UserDetail.objects.get( user = self )
        return self.username

class UserDetail( models.Model ):
    user = models.OneToOneField( ActionUser )
    callSign = models.CharField( max_length = 20, null = True, blank = True )
    deviceType = models.CharField( max_length = 40, null = True, blank = True )
    deviceModel = models.CharField( max_length = 40, null = True, blank = True )
    radioServer = models.CharField( max_length = 40, null = True, blank = True )
    firstName = models.CharField( max_length = 40, null = True, blank = True )
    lastName = models.CharField( max_length = 40, null = True, blank = True )
    organization = models.CharField( max_length = 40, null = True, blank = True )
    epicNumber = models.CharField( max_length = 10, null = True, blank = True )
    inactiveUser = models.BooleanField( blank = True )
    sipAddress = models.CharField( max_length = 80, null = True, blank = True )
    emailAddress = models.EmailField(blank=True,null=True)
    timeZone = models.IntegerField( null = True, blank = True )
    objects = models.GeoManager()

    def __unicode__( self ):
        theStr = '%s %s' % ( self.firstName, self.lastName )
        if theStr == 'None None':
            theStr = self.user.username
        if self.organization:
            theStr = '%s - %s' % ( theStr, self.organization )
        if self.emailAddress:
            theStr = '%s - %s' % ( theStr, self.emailAddress )
        return theStr

class Position( models.Model ):
    user = models.ForeignKey( ActionUser, db_column = 'FK_Users_ID' )
    icon = models.ForeignKey( Icon, db_column = 'FK_Icons_ID', blank = True,null=True )
    altitude = models.FloatField( null = True, db_column = 'Altitude', blank = True )
    speed = models.FloatField( null = True, db_column = 'Speed', blank = True )
    angle = models.FloatField( null = True, db_column = 'Angle', blank = True )
    dateadded = models.DateTimeField( db_column = 'DateAdded' , blank = True ,null = True)
    dateoccurred = models.DateTimeField( null = True, db_column = 'DateOccurred', blank = True )
    comments = models.TextField( max_length = 765, db_column = 'Comments', blank = True, null=True )
    imageurl = models.ImageField(upload_to='c:/epic/tracker/media/images', max_length = 765, db_column = 'ImageURL', null = True,blank = True )
    signalstrength = models.IntegerField( null = True, db_column = 'SignalStrength', blank = True )
    signalstrengthmax = models.IntegerField( null = True, db_column = 'SignalStrengthMax', blank = True )
    signalstrengthmin = models.IntegerField( null = True, db_column = 'SignalStrengthMin', blank = True )
    batterystatus = models.IntegerField( null = True, db_column = 'BatteryStatus', blank = True )
    location = models.PointField( null = True, blank = True)
    
    objects = models.GeoManager()
    class Meta:
        db_table = u'positions'
    def __unicode__( self ):
        return '%s "%s" %s' % ( self.user, self.dateoccurred, self.latitude )
    
    @property
    def longitude(self):
        return self.location.get_x()

    @property
    def latitude(self):
        return self.location.get_y()

class CurrentPosition( models.Model ):
    user = models.OneToOneField( ActionUser )
    position = models.ForeignKey( Position )
    objects = models.GeoManager()
    
    def __unicode__(self):
        return self.user 



### NEW CLASSES   
class RadioServer(models.Model):
    serverName = models.CharField(max_length = 100)
    latestUpdate = models.DateTimeField(blank=True, null=True)
    latestCheck = models.DateTimeField(blank=True, null=True)
    serverEnabled = models.BooleanField(default=True)
    refreshPeriod = models.IntegerField(default = 300)
    objects = models.GeoManager()
    
    def __unicode__(self):
        return self.serverName 

    
class LoggingList(models.Model):
    reportingServer = models.CharField(max_length=20, blank=True, null=True, help_text="")
    errorText = models.CharField(max_length=100, blank=True, null=True, help_text="")
    actionDate = models.DateTimeField( blank=True, null=True, auto_now_add=True)
    def __unicode__(self):
        return self.serverName + "  " + errorText 
    
class Incident(models.Model):
    user = models.ForeignKey(ActionUser)    
    image = models.ImageField(upload_to=".",blank=True,null=True)
    image_ref = models.CharField(max_length=50, blank=True, null=True, help_text="dont use")
    description = models.TextField(blank=True,null=True)
    location = models.PointField(help_text="POINT(LON LAT)",blank=True,null=True)
    date_reported = models.DateTimeField( blank = True ,null = True)
    actionDate = models.DateTimeField( blank=True, null=True, auto_now_add=True)
    objects = models.GeoManager()
    
    def __unicode__(self):
        longitude = ""
        latitude = ""
        try:
            longitude = self.location.get_x()
            latitude =self.location.get_y()
            return "%s Lon:%f Lat:%f"%(self.description ,longitude,latitude)
        except:
            return "%s Lon:%s Lat:%s"%(self.description ,longitude,latitude)
        
        
    @property
    def longitude(self):
        return self.location.get_x()

    @property
    def latitude(self):
        return self.location.get_y()


class GeoFence(models.Model):
    name = models.CharField( max_length=200 , blank=True, null=True, help_text="Name of Fence")
    type = models.CharField(choices=FENCE_TYPE, max_length=50, blank=True, null=True, help_text="Type Of Fence")
    description = models.TextField(blank=True, help_text="Describe Fence")
    warningIn = models.CharField(verbose_name="Warning Text In", max_length=144, blank=True, null=True, help_text="Alert sent on entry")
    warningOut = models.CharField( max_length=144, blank=True, null=True, help_text="Alert sent on exit")
    fence = models.PolygonField()
    objects = models.GeoManager()
    def __unicode__(self):
        return self.name
    

### TO BE REMOVED
class Trip(models.Model):
    user = models.ForeignKey(ActionUser, db_column = 'FK_Users_ID')
    name = models.CharField( max_length = 255, null = True, blank = True )
    comments = models.TextField( max_length = 1024, null = True, blank = True )
    objects = models.GeoManager()
    class Meta:
            db_table = u'trips'


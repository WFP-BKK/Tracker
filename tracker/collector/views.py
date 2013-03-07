# Create your views here.
#from tracker.datastore.models import *
import datetime, urllib2
from django.utils.timezone import utc
from dateutil import parser
from dateutil import tz
from xml.dom.minidom import parse, parseString
from datastore.models import Position, CurrentPosition, ActionUser,Icon,Trip, Incident
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from urllib import unquote
from settings import MEDIA_ROOT
from django.shortcuts import render_to_response
from django.forms.models import modelform_factory
from django.views.decorators.csrf import csrf_exempt
    
import warnings
warnings.filterwarnings(
        'error', r"DateTimeField received a naive datetime",
        RuntimeWarning, r'django\.db\.models\.fields')

#"GET /trackme/requests.php?a=upload&u=wgonzalez&p=wfpdubai&lat=25.18511038&long=55.29178735&do=2011-2-3%2013:12:3&tn=wgonzalez&alt=7&ang=&sp=&db=8 HTTP/1.1"
#"GET /trackme/requests.php?a=gettriplist&u=wgonzalez&p=wfpdubai&db=8 HTTP/1.1" 200 16
#"POST /trackme/upload.php?u=wgonzalez&p=wfpdubai&db=8&a=pic&newname=wgonzalez14736.jpg& HTTP/1.1" 200 8
#"GET /trackme/requests.php?a=upload&u=wgonzalez&p=wfpdubai&lat=25.18515436&long=55.29165062&do=2011-8-8%2014:7:46&tn=A&alt=2.9&ang=100.6&sp=&comments=tteest&imageurl=http://10.11.208.39:8000/trackme/pics/wgonzalez14736.jpg&db=8 HTTP/1.1" 200 8
#"GET /trackme/gm.php?lat=25.18506629&long=55.29138774 HTTP/1.1" 404 3117
#"GET /trackme/export.php?a=kml&u=wgonzalez&p=wfpdubai&tn=%3CNone%3E&db=8 HTTP/1.1" 404 3156
#"GET /trackme/requests.php?a=upload&u=wgonzalez&p=wfpdubai&lat=25.18505015&long=55.29139479&do=2011-8-8%2014:12:21&tn=test&alt=36.9&ang=100.6&sp=&db=8 HTTP/1.1" 200 8
#"GET /trackme/export.php?a=kml&u=wgonzalez&p=wfpdubai&tn=test&df=2011-8-8%208:14:19&dt=2011-8-8%2015:14:19&sb=1&db=8 HTTP/1.1" 404 3212
#"GET /trackme/export.php?a=gpx&u=wgonzalez&p=wfpdubai&tn=test&df=2011-8-8%208:14:19&dt=2011-8-8%2015:14:19&sb=1&db=8 HTTP/1.1" 404 3212
#"GET /trackme/requests.php?a=geticonlist&u=wgonzalez&p=wfpdubai&db=8 HTTP/1.1" 200 14
#"GET /trackme/requests.php?a=gettriplist&u=wgonzalez&p=wfpdubai&db=8 HTTP/1.1" 200 16
#/trackme/requests.php?a=updateimageurl&u=wgonzalez&p=wfpdubai&id=0&imageurl=http://10.11.208.20:80/trackme/pics/wgonzalez1583.jpg&db=8 
#Time zone http://www.earthtools.org/timezone-1.1/40.71417/-74.00639 (lat/long)
def collect( request ): #request.php
    """
    The Collector:
    #"GET /trackme/requests.php?a=upload&u=wgonzalez&p=wfpdubai&lat=25.18511038&long=55.29178735&do=2011-2-3%2013:12:3&tn=wgonzalez&alt=7&ang=&sp=&db=8 HTTP/1.1"
    #"GET /trackme/requests.php?a=gettriplist&u=wgonzalez&p=wfpdubai&db=8 HTTP/1.1" 200 16
    #"POST /trackme/upload.php?u=wgonzalez&p=wfpdubai&db=8&a=pic&newname=wgonzalez14736.jpg& HTTP/1.1" 200 8
    #"GET /trackme/requests.php?a=upload&u=wgonzalez&p=wfpdubai&lat=25.18515436&long=55.29165062&do=2011-8-8%2014:7:46&tn=A&alt=2.9&ang=100.6&sp=&comments=tteest&imageurl=http://10.11.208.39:8000/trackme/pics/wgonzalez14736.jpg&db=8 HTTP/1.1" 200 8
    #"GET /trackme/gm.php?lat=25.18506629&long=55.29138774 HTTP/1.1" 404 3117
    #"GET /trackme/export.php?a=kml&u=wgonzalez&p=wfpdubai&tn=%3CNone%3E&db=8 HTTP/1.1" 404 3156
    #"GET /trackme/requests.php?a=upload&u=wgonzalez&p=wfpdubai&lat=25.18505015&long=55.29139479&do=2011-8-8%2014:12:21&tn=test&alt=36.9&ang=100.6&sp=&db=8 HTTP/1.1" 200 8
    #"GET /trackme/export.php?a=kml&u=wgonzalez&p=wfpdubai&tn=test&df=2011-8-8%208:14:19&dt=2011-8-8%2015:14:19&sb=1&db=8 HTTP/1.1" 404 3212
    #"GET /trackme/export.php?a=gpx&u=wgonzalez&p=wfpdubai&tn=test&df=2011-8-8%208:14:19&dt=2011-8-8%2015:14:19&sb=1&db=8 HTTP/1.1" 404 3212
    #"GET /trackme/requests.php?a=geticonlist&u=wgonzalez&p=wfpdubai&db=8 HTTP/1.1" 200 14
    #"GET /trackme/requests.php?a=gettriplist&u=wgonzalez&p=wfpdubai&db=8 HTTP/1.1" 200 16
    #/trackme/requests.php?a=updateimageurl&u=wgonzalez&p=wfpdubai&id=0&imageurl=http://10.11.208.20:80/trackme/pics/wgonzalez1583.jpg&db=8
    """
    user = ''
    id = ''
    latitude = ''
    longitude = ''
    date = ''
    altitude = 0
    image = ''
    comments = ''
    myIconID = int()

    action = request.GET.get('a')

    ## Utility functions
    if action == 'geticonlist':
        mystring ='Result:0'
        icons = Icon.objects.all()
        for icon in icons:
            mystring += '|' + icon.name
        return HttpResponse( mystring )

    # Get Positions:
    try:
        latitude = request.GET.get( 'lat' )
        longitude = request.GET.get( 'long' )
        altitude = request.GET.get( 'alt' )
        if altitude=='':
            altitude = 0
    except:
        pass

    #Get Dates

    try:
        do_date = unquote(request.GET.get( 'do' ))
    except:
        pass

    try:
        user = request.GET.get( 'u' )

        if action != 'updateimageurl':
            id = request.GET.get('id')
            if id:
                try:
                    user = ActionUser.objects.get(id= id).username
                except:
                     user = id
            #get the user
        if id:
            myUser, new_user = ActionUser.objects.get_or_create( id= id, username = user )
        else:
            myUser, new_user = ActionUser.objects.get_or_create( username = user )
        
    
    except:
        pass

    try:
        image = request.GET.get('imageurl')
        image = fixurl(image)
    except:
        pass

    try:
        comments = request.GET.get('comments')
    except:
        pass

    try:
        icon = request.GET.get('iconname')
        theIcon = Icon.objects.get(name=icon)
        if theIcon:
            myIconID = theIcon.id

    except:
            pass

    if action == 'upload':
        #add online timeShift per location
        saved = save_point(myUser,do_date, latitude,longitude,altitude,image,comments,myIconID)
        if saved:
            return HttpResponse( 'Result:0' )
        else:
            return HttpResponse( 'Result:1' )


    if action == 'gettriplist':
        mystring ='Result:0'
        trips = Trip.objects.filter(user=myUser)
        for trip in trips:
            mystring += '|' + trip.name + '|%s\n'%datetime.date.today().isoformat()
        return HttpResponse( mystring.strip() )

    if action == 'updateimageurl':
        return HttpResponse( 'Result:0' )

    if action == 'findclosestpositionbytime':
        date = request.GET.get( 'date' )
        return HttpResponse('Result:0|0|%s'%date)    #return HttpResponse( 'Result:6' ) # no date....

    return HttpResponse( 'Result:1' )


def save_point(myUser,do_date, latitude,longitude,altitude,image,comments,myIconID):
        myPoints=''
        location = "POINT("+str(longitude) + " "+ str(latitude) +")"
        tdate = parser.parse(do_date)
        time_now = datetime.datetime.utcnow().replace(tzinfo=utc)
        try:#brutal check if date is timezoned else add timezone
            ta = tdate - time_now
        except:
            timeShift = myUser.userdetail.timeZone
            if timeShift !=0 :
                timeZoneHere = tz.tzoffset("abc",timeShift*60*60)
                tdate = tdate.replace(tzinfo=timeZoneHere)
            else:
                tdate = tdate.replace(tzinfo=utc)

        myPoints , new_position = Position.objects.get_or_create( 
                                                     dateoccurred = tdate,
                                                     user = myUser,
                                                     latitude = latitude,
                                                     longitude = longitude,
                                                     altitude = altitude,
                                                     imageurl = image,
                                                     comments = comments,
                                                     location = location,
                                                     defaults = {'dateadded':time_now })
        if myIconID:
            myPoints.icon = theIcon
            myPoints.save()
        if new_position:
            cpos, new_cp = CurrentPosition.objects.get_or_create( user = myUser, defaults = {'position':myPoints} )
            cpos.position = myPoints
            cpos.save()
            return True
        else:
            return False



def fixurl(string):
    url = string.split('/')
    return url[-1]

def update_current( request ):
    return HttpResponse( 'Result:0' )


def handle_uploaded_file(f,name):
    destination = open(MEDIA_ROOT +'/' +name, 'wb+')
    for chunk in f.chunks():
        destination.write(chunk)
    destination.close()
        
@csrf_exempt    
def upload( request):#upload.php
    handle_uploaded_file(request.FILES['uploadfile'],request.GET['newname'])
    return HttpResponse( 'Result:0' )

@csrf_exempt    
def export( request):#upload.php
    print 'Export not yet implemented'
    return HttpResponse( '<Result>0</Result>' )



@csrf_exempt
def create_incident(request):
    IncedentForm = modelform_factory(Incident)

    if request.method == 'POST':
        print request.POST
        try:
            user = ActionUser.objects.get(id = request.POST['user'])
        except:
            request.POST['user'] =  ActionUser.objects.get(username = request.POST['user']).id
        form =  IncedentForm(request.POST, request.FILES)
        if form.is_valid():
                form.save()
                return HttpResponse( 'Result:0' )
    else:
        form = IncedentForm()
        
    return render_to_response('incident.html',{'form':form})
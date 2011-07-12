# Create your views here.
from datastore.models import CurrentPosition, ActionUser, Position
from django.shortcuts import render_to_response
import datetime
from django.views.decorators.csrf import csrf_exempt
#from django.template import Template, RequestContext,Library, Node, loader, Context


@csrf_exempt
def all_points( request ):
    datefilter = datetime.datetime.now() + datetime.timedelta( days = -7 )
    dayfilter = datetime.datetime.now() + datetime.timedelta( days = -2 )
    myUsers = Position.objects.all()
    points = []
    try:
        theFilter = request.GET.get( 'filter' )
    except:
        theFilter = ''
    for the_user in myUsers:
        try:
            inactive = the_user.user.userdetail.inactiveUser
        except:
            inactive = False
        if not inactive:
            if theFilter == 'all':
                if the_user.position.dateoccurred > dayfilter:
                    the_user.pin = 'current'
                else:
                    the_user.pin = 'old'
                points.append( the_user )
            else:
                if the_user.user.details.inactiveUser != True:
                    if the_user.position.dateoccurred > datefilter:
                        if the_user.position.dateoccurred > dayfilter:
                            the_user.pin = 'current'
                        else:
                            the_user.pin = 'old'
                        points.append( the_user )
    my_response = render_to_response( 'listit.xml', {'list':points}, mimetype = "application/xml" )
    my_response['Access-Control-Allow-Origin'] = '*'
# Access-Control-Allow-Methods: GET, POST, OPTIONS
# Access-Control-Allow-Headers: Content-Type
# Access-Control-Max-Age: 86400
    return my_response


@csrf_exempt
def all_points_kml( request ):
    datefilter = datetime.datetime.now() + datetime.timedelta( days = -7 )
    dayfilter = datetime.datetime.now() + datetime.timedelta( days = -1 )
    myUsers = CurrentPosition.objects.all()
    points = []
    for the_user in myUsers:
        if the_user.position.dateoccurred > datefilter:
            if the_user.position.dateoccurred > dayfilter:
                the_user.pin = 'here'
            else:
                the_user.pin = 'bar'
            points.append( the_user )

    my_response = render_to_response( 'kml_repr.kml', {'list':points}, mimetype = "application/xml" )
    my_response['Access-Control-Allow-Origin'] = '*'
# Access-Control-Allow-Methods: GET, POST, OPTIONS
# Access-Control-Allow-Headers: Content-Type
# Access-Control-Max-Age: 86400
    return my_response


@csrf_exempt
def all_paths_kml( requst ):
    theUsers = ActionUser.objects.all()
    #points for the last 10w
    datefilter = datetime.datetime.now() + datetime.timedelta( days = -70 )
    for user in theUsers:
        allPoints = Position.objects.filter( user = user ).order_by( '-dateoccurred' ).filter( dateoccurred__gt = datefilter )

        if  allPoints.count() > 3:
            user.hasPath = True
            user.path = allPoints
            print '%s %s' % ( user, allPoints.count() )
            user.lastPoint = allPoints[allPoints.count() - 1]
        #else:
        #    print user

    my_response = render_to_response( 'kml_paths.kml', {'users':theUsers}, mimetype = "application/xml" )
    my_response['Access-Control-Allow-Origin'] = '*'
# Access-Control-Allow-Methods: GET, POST, OPTIONS
# Access-Control-Allow-Headers: Content-Type
# Access-Control-Max-Age: 86400
    return my_response




# Create your views here.
from datastore.models import CurrentPosition, ActionUser, Position,Icon
from django.shortcuts import render_to_response
import datetime
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
#from django.template import Template, RequestContext,Library, Node, loader, Context


@csrf_exempt
def all_points( request ):
    datefilter = datetime.datetime.now() + datetime.timedelta( days = -7 )
    dayfilter = datetime.datetime.now() + datetime.timedelta( days = -2 )
    myUsers = CurrentPosition.objects.all()
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
			try:
				if theFilter == 'all':
					if the_user.position.dateoccurred > dayfilter:
						the_user.pin = 'current'
					else:
						the_user.pin = 'old'
					points.append( the_user )
				else:
					if not inactive:
						if the_user.position.dateoccurred > datefilter:
							if the_user.position.dateoccurred > dayfilter:
								the_user.pin = 'current'
							else:
								the_user.pin = 'old'
							points.append( the_user )
			except:
				pass				
    my_response = render_to_response( 'listit.xml', {'list':points}, mimetype = "application/xml" )
    my_response['Access-Control-Allow-Origin'] = '*'
    return my_response

@csrf_exempt
def show_poi(request):
    thePositions = Position.objects.all()
    thePointsOfIntrest = thePositions.filter(icon__isnull=False).exclude(icon =33)
    thePhotos = thePositions.filter(imageurl__isnull=False).exclude(imageurl__exact='')
    theComments = thePositions.filter(comments__isnull=False).exclude(comments__exact='')
    myPoints= list(set(thePointsOfIntrest)|set(thePhotos)|set(theComments))
    my_response = render_to_response( 'poi.kml', {'poi':myPoints}, mimetype = "application/xml" )
    my_response['Access-Control-Allow-Origin'] = '*'
    return my_response

@csrf_exempt    
def show_poi_rss(request):
    thePositions = Position.objects.all()
    thePointsOfIntrest = thePositions.filter(icon__isnull=False).exclude(icon =33)
    thePhotos = thePositions.filter(imageurl__isnull=False).exclude(imageurl__exact='')
    theComments = thePositions.filter(comments__isnull=False).exclude(comments__exact='')
    myPoints= list(set(thePointsOfIntrest)|set(thePhotos)|set(theComments))
    my_response = render_to_response( 'poi.rss', {'poi':myPoints}, mimetype = "application/xml" )
    my_response['Access-Control-Allow-Origin'] = '*'
    return my_response
    

@csrf_exempt    
def show_images_rss(request):
    thePositions = Position.objects.all()
    thePhotos = thePositions.filter(imageurl__isnull=False).exclude(imageurl__exact='')
    myPoints= list(set(thePhotos))
    my_response = render_to_response( 'poi.rss', {'poi':myPoints}, mimetype = "application/xml" )
    my_response['Access-Control-Allow-Origin'] = '*'
    return my_response

@csrf_exempt
def all_points_kml( request ):
    datefilter = datetime.datetime.now() + datetime.timedelta( days = -7 )
    dayfilter = datetime.datetime.now() + datetime.timedelta( days = -1 )
    myUsers = CurrentPosition.objects.all()
    points = []
    for the_user in myUsers:
        try:
			if the_user.position.dateoccurred > datefilter:
				if the_user.position.dateoccurred > dayfilter:
					the_user.pin = 'here'
				else:
					the_user.pin = 'bar'
				points.append( the_user )
        except:
			pass
    my_response = render_to_response( 'kml_repr.kml', {'list':points}, mimetype = "application/xml" )
    my_response['Access-Control-Allow-Origin'] = '*'
    return my_response

@csrf_exempt
def all_points_json( request ):
    datefilter = datetime.datetime.now() + datetime.timedelta( days = -7 )
    dayfilter = datetime.datetime.now() + datetime.timedelta( days = -1 )
    myUsers = CurrentPosition.objects.all()
    points = []
    for the_user in myUsers:
        try:
            if the_user.position.dateoccurred > datefilter:
                if the_user.position.dateoccurred > dayfilter:
                    the_user.pin = 'here'
                else:
                    the_user.pin = 'bar'
                points.append( the_user )
        except:
            pass
    data = serializers.serialize("json", points,ensure_ascii=False)
    my_response = render_to_response( 'kml_repr.kml', {'list':points}, mimetype = "application/xml" )
    my_response['Access-Control-Allow-Origin'] = '*'
    return my_response


@csrf_exempt
def all_points_rss( request ):
    datefilter = datetime.datetime.now() + datetime.timedelta( days = -7 )
    dayfilter = datetime.datetime.now() + datetime.timedelta( days = -1 )
    myUsers = CurrentPosition.objects.all()
    points = []
    for the_user in myUsers:
        try:
            if not the_user.user.userdetail.inactiveUser:
                try:
                    if the_user.position.dateoccurred > datefilter:
                        if the_user.position.dateoccurred > dayfilter:
                            the_user.pin = 'here'
                        else:
                            the_user.pin = 'bar'
                        points.append( the_user )
                except:
                    pass
        except:
                    pass
    my_response = render_to_response( 'rss_repr.rss', {'list':points}, mimetype = "application/xml" )
    my_response['Access-Control-Allow-Origin'] = '*'
    return my_response


@csrf_exempt
def all_paths_kml( requst ):
    theUsers = ActionUser.objects.all()
    #points for the last 10w
    datefilter = datetime.datetime.now() + datetime.timedelta( days = -200 )
    for user in theUsers:
        try:
			allPoints = Position.objects.filter( user = user ).order_by( '-dateoccurred' ).filter( dateoccurred__gt = datefilter )
	
			if  allPoints.count() > 3:
				user.hasPath = True
				user.path = allPoints[:40]
				user.lastPoint = allPoints[allPoints.count() - 1]
        except:
			pass

    my_response = render_to_response( 'kml_paths.kml', {'users':theUsers}, mimetype = "application/xml" )
    my_response['Access-Control-Allow-Origin'] = '*'

    return my_response

def all_paths_rss( requst ):
    theUsers = ActionUser.objects.all()
    #points for the last 10w
    datefilter = datetime.datetime.now() + datetime.timedelta( days = -200 )
    for user in theUsers:
        try:
			allPoints = Position.objects.filter( user = user ).order_by( '-dateoccurred' ).filter( dateoccurred__gt = datefilter )[:10]
			if  allPoints.count() > 3:
				user.hasPath = True
				user.path = allPoints[:40]
				user.lastPoint = allPoints[allPoints.count() - 1]
        except:
			pass
    my_response = render_to_response( 'rss_paths.rss', {'users':theUsers}, mimetype = "application/xml" )
    my_response['Access-Control-Allow-Origin'] = '*'
    return my_response

def one_path_rss( requst,user ):
#    theUsers = ActionUser.objects.all()
    theUsers = ActionUser.objects.filter(username=user)
    #points for the last 10w
    datefilter = datetime.datetime.now() + datetime.timedelta( days = -200 )
    for user in theUsers:
        try:
			allPoints = Position.objects.filter( user = user ).order_by( '-dateoccurred' )#.filter( dateoccurred__gt = datefilter )
			if  allPoints.count() > 3:
				user.hasPath = True
				user.path = allPoints[:40]
				user.lastPoint = allPoints[allPoints.count() - 1]
        except:
			pass
    my_response = render_to_response( 'rss_paths.rss', {'users':theUsers}, mimetype = "application/xml" )
    my_response['Access-Control-Allow-Origin'] = '*'
    return my_response



def get_styles(request):
    theIcons = Icon.objects.all()
    my_response = render_to_response( 'style.kml', {'icons':theIcons}, mimetype = "application/xml" )
    my_response['Access-Control-Allow-Origin'] = '*'

    return my_response

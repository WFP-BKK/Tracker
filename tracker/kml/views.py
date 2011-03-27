# Create your views here.
from tracker.datastore.models import CurrentPosition, ActionUser, Position
from django.shortcuts import render_to_response
import datetime
#from django.template import Template, RequestContext,Library, Node, loader, Context


def all_points(request):
    datefilter = datetime.datetime.now() + datetime.timedelta(days= -7)
    dayfilter = datetime.datetime.now() + datetime.timedelta(days= -2)
    myUsers = CurrentPosition.objects.all()
    points = []
    theFilter = request.GET.get('filter')
    for the_user in myUsers:
        if theFilter == 'all':
            if the_user.position.dateoccurred > dayfilter:
                the_user.pin = 'current'
            else:
                the_user.pin = 'old'
            points.append(the_user)
        else:
            if the_user.user.inactiveUser == False:
                if the_user.position.dateoccurred > datefilter:
                    if the_user.position.dateoccurred > dayfilter:
                        the_user.pin = 'current'
                    else:
                        the_user.pin = 'old'
                    points.append(the_user)                
    return render_to_response('listit.xml', {'list':points}, mimetype="text/xml")

def all_points_kml(request):
    datefilter = datetime.datetime.now() + datetime.timedelta(days= -7)
    dayfilter = datetime.datetime.now() + datetime.timedelta(days= -1)
    myUsers = CurrentPosition.objects.all()
    points = []
    for the_user in myUsers:
        if the_user.position.dateoccurred > datefilter:
            if the_user.position.dateoccurred > dayfilter:
                the_user.pin = 'here'
            else:
                the_user.pin = 'bar'
            points.append(the_user)
                
    return render_to_response('kml_repr.kml', {'list':points}, mimetype="text/xml")

def all_paths_kml(requst):
    theUsers = ActionUser.objects.all()
    #points for the last 10w
    datefilter = datetime.datetime.now() + datetime.timedelta(days= -70)
    for user in theUsers:
        allPoints = Position.objects.filter(user=user).order_by('-dateoccurred').filter(dateoccurred__gt = datefilter)
        
        if  allPoints.count() > 3:
            user.hasPath=True
            user.path = allPoints
            print '%s %s' % (user,allPoints.count())
            user.lastPoint = allPoints[allPoints.count()-1]
        #else:
        #    print user
        

    return render_to_response('kml_paths.kml', {'users':theUsers}, mimetype="text/xml")





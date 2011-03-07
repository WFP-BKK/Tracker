# Create your views here.
from tracker.datastore.models import CurrentPosition
from django.shortcuts import render_to_response
import datetime
#from django.template import Template, RequestContext,Library, Node, loader, Context


def all_points(request):
    datefilter = datetime.datetime.now()+datetime.timedelta(days=-7)
    dayfilter =  datetime.datetime.now()+datetime.timedelta(days=-2)
    myUsers = CurrentPosition.objects.all()
    points=[]
    theFilter = request.GET.get('filter')
    for the_user in myUsers:
        if theFilter == 'all':
            if the_user.position.dateoccurred > dayfilter:
                the_user.pin = 'current'
            else:
                the_user.pin = 'old'
            points.append(the_user)
        else:
            if the_user.position.dateoccurred > datefilter:
                if the_user.position.dateoccurred > dayfilter:
                    the_user.pin = 'current'
                else:
                    the_user.pin = 'old'
                points.append(the_user)
                
                
    return render_to_response('listit.xml',{'list':points},mimetype="text/xml")

def all_points_kml(request):
    datefilter = datetime.datetime.now()+ datetime.timedelta(days=-7)
    dayfilter =  datetime.datetime.now()+datetime.timedelta(days=-1)
    myUsers = CurrentPosition.objects.all()
    points=[]
    for the_user in myUsers:
        if the_user.position.dateoccurred > datefilter:
            if the_user.position.dateoccurred > dayfilter:
                the_user.pin = 'here'
            else:
                the_user.pin = 'bar'
            points.append(the_user)
                
    return render_to_response('kml_repr.kml',{'list':points},mimetype="text/xml")


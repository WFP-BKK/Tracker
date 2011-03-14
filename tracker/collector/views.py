# Create your views here.
#from tracker.datastore.models import *
import datetime
from tracker.datastore.models import Position, CurrentPosition, ActionUser
from django.http import HttpResponse
#"GET /trackme/requests.php?a=upload&u=wgonzalez&p=wfpdubai&lat=25.18511038&long=55.29178735&do=2011-2-3%2013:12:3&tn=wgonzalez&alt=7&ang=&sp=&db=8 HTTP/1.1"
#Result:0

def collect(request):
    user = ''
    latitude = ''
    longitude = ''
    date = ''
    altitude = ''
    try:
        user = request.GET.get('u')
        latitude = request.GET.get('lat')
        longitude = request.GET.get('long')
        date = request.GET.get('do')
        altitude = request.GET.get('alt')
    except:
        pass
    #get the user
    
    myUser, new_user = ActionUser.objects.get_or_create(username=user)
    myPoints , new_position = Position.objects.get_or_create(
                                                 dateoccurred=date,
                                                 user=myUser,
                                                 latitude=latitude,
                                                 longitude=longitude,
                                                 altitude=altitude,
                                                 defaults={'dateadded':datetime.datetime.now()})

    if new_position:
        cpos, new_cp = CurrentPosition.objects.get_or_create(user=myUser, defaults={'position':myPoints})
        cpos.position = myPoints
        cpos.save()
        return HttpResponse('Result:0')    
    else:
        return HttpResponse('Result:1')
    print new_user, new_cp
    
def update_current(request):
    allUsers = ActionUser.objects.all()
    for theUser in allUsers:
        myPosition = Position.objects.filter(user=theUser).order_by('-dateoccurred')
        if myPosition:
            myCurrent, ok = CurrentPosition.objects.get_or_create(user=theUser, defaults={'position':myPosition[0]})
            print ok
            myCurrent.position = myPosition[0]
            myCurrent.save()
    return HttpResponse('Result:0')


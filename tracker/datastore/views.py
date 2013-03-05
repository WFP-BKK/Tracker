from django.forms.models import modelform_factory
from models import *
from django.shortcuts import render_to_response




def create_incident(request):
    IncedentForm = modelform_factory(Incident)
    if request.method == 'POST':
        form =  IncedentForm(request.POST, request.FILES)
        if form.is_valid():
            pass
    else:
        form = IncedentForm()
        
    return render_to_response('incident.html',{'form':form})
    

from django.conf.urls import patterns
from django.views.generic.base import TemplateView
import settings
from django.contrib.auth.decorators import login_required

class MapTemplateView(TemplateView):
        template_name = "map 2.html"
        
        def get_context_data(self, **kwargs):
            context = super(MapTemplateView, self).get_context_data(**kwargs)
            context['sensory_url'] = settings.SENSOR_URL
            context['server_type'] = settings.SERVER_TYPE
            return context


urlpatterns = patterns( 
                       '',
                       ( r'^$', login_required(MapTemplateView.as_view(template_name='map 2.html') )),
                       ( r'^incidents$', TemplateView.as_view(template_name='incidents.html') ),
                       ( r'^upload$', TemplateView.as_view(template_name='upload.html') ),

 )

from django.conf.urls.defaults import patterns
from tracker.settings import STATIC_DOC_ROOT
from django.views.generic.simple import redirect_to, direct_to_template
urlpatterns = patterns( 
                       '',
                       ( r'^$', 'direct_to_template', {'template': 'map.html'} ),
                       ( r'^plain$', 'direct_to_template', {'template': 'map_plain.html'} ),
                       ( r'^kml/$', 'direct_to_template', {'template': 'map.html'} ),
                       ( r'^images/(?P<path>.*)$', 'django.views.static.serve', {'document_root': STATIC_DOC_ROOT} ),

 )

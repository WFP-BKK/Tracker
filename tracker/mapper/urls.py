from django.conf.urls.defaults import patterns
from settings import STATIC_DOC_ROOT
from django.views.generic.simple import redirect_to, direct_to_template
urlpatterns = patterns( 
                       '',
                       ( r'^$', 'django.views.generic.simple.direct_to_template', {'template': 'map.html'} ),
    ( r'^new$', 'django.views.generic.simple.direct_to_template', {'template': 'map2.html'} ),
                       ( r'^plain$', 'django.views.generic.simple.direct_to_template', {'template': 'map_plain.html'} ),
                       ( r'^kml/$', 'django.views.generic.simple.direct_to_template', {'template': 'map.html'} ),
                       ( r'^images/(?P<path>.*)$', 'django.views.static.serve', {'document_root': STATIC_DOC_ROOT} ),

 )

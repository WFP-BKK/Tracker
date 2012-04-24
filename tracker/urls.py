from django.conf.urls.defaults import patterns, include
from collector.views import *
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
from settings import MEDIA_ROOT

urlpatterns = patterns( '',
    ( r'^admin/', include( admin.site.urls ) ),
    ( r'^mapper/', include( 'mapper.urls' ) ),
    ( r'^kml', include( 'kml.urls' ) ),
    ( r'^trackme/', include( 'collector.urls' ) ),
    ( r'^upload.php', 'collector.views.upload' ),
     ( r'^requests.php', 'collector.views.collect' ),
    ( r'^trackme/media/(?P<path>.*)$', 'django.views.static.serve',
    {'document_root': MEDIA_ROOT} ),
    ( r'^media/(?P<path>.*)$', 'django.views.static.serve',
    {'document_root': MEDIA_ROOT} ),
    ( r'^$', 'django.views.generic.simple.redirect_to', {'url': 'mapper/'} ),
 )

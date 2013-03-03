from django.conf.urls.defaults import patterns, include
from collector.views import *
from django.views.generic.base import RedirectView
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
    ( r'^$', RedirectView.as_view(url= 'mapper/')),
 )

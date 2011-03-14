from django.conf.urls.defaults import patterns, include
from tracker.collector.views import *
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
from tracker.settings import MEDIA_ROOT

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    (r'^mapper/', include('tracker.mapper.urls')),
    (r'^kml', include('tracker.kml.urls')),
    (r'^trackme/', include('tracker.collector.urls')),
     (r'^requests.php', 'tracker.collector.views.collect')
    (r'^trackme/media/(?P<path>.*)$', 'django.views.static.serve',
    {'document_root': MEDIA_ROOT}),
)

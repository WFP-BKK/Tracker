from django.conf.urls.defaults import patterns,include

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
from tracker.settings import MEDIA_ROOT

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    (r'^maper/', include('tracker.mapper.urls')),
    (r'^kml', include('tracker.kml.urls')),
    (r'^trackme/', include('tracker.collector.urls')),
    (r'^trackme/media/(?P<path>.*)$', 'django.views.static.serve',
    {'document_root': MEDIA_ROOT}),
)

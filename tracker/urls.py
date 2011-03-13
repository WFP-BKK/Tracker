from django.conf.urls.defaults import patterns, include

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
from tracker.settings import MEDIA_ROOT

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    (r'^mapper/', include('mapper.urls')),
    (r'^kml', include('kml.urls')),
    (r'^trackme/', include('collector.urls')),
    (r'^trackme/media/(?P<path>.*)$', 'django.views.static.serve',
    {'document_root': MEDIA_ROOT}),
)

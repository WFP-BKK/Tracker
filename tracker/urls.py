from django.conf.urls.defaults import patterns,include

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    (r'^map/', include('tracker.mapper.urls')),
    (r'^kml', include('tracker.kml.urls')),
    (r'^trackme/', include('tracker.collector.urls')),
)

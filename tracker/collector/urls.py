from django.conf.urls.defaults import  patterns


urlpatterns = patterns( 
                       '',
                       ( r'^requests.php', 'collector.views.collect' ),
                       ( r'^update/', 'collector.views.update_current' ),
                       ( r'^upload.php', 'collector.views.upload' ),
                       ( r'^export.php', 'collector.views.export' ),
                       #( r'^gm.php', 'mapper.views.gm' ),
                       ( r'^radio_check/(?P<radio_id>.*)$', 'collector.views.radioserver_update_now' ),
                       ( r'^radio_error/(?P<radio_id>.*)$', 'collector.views.radioserver_error' ),
                       ( r'^radio_update/(?P<radio_id>.*)/(?P<device_id>.*)/(?P<latitude>.*)/(?P<longitude>.*)/$', 'collector.views.update_radio_positions' ),
 )

from django.conf.urls import  patterns


urlpatterns = patterns( 
                       '',
                       ( r'^requests.php', 'collector.views.collect' ),
                       ( r'^update/', 'collector.views.update_current' ),( r'^trackme/update/', 'collector.views.update_current' ), 
                      ( r'^upload.php', 'collector.views.upload' ),
                       ( r'^export.php', 'collector.views.export' ),
                       ( r'^kml.rss', 'kml.views.all_points_rss'),
                       ( r'^radio_check/(?P<radio_id>.*)$', 'collector.views.radioserver_update_now' ),
                       ( r'^radio_force/(?P<radio_id>.*)$', 'collector.views.request_update' ),
                       ( r'^radio_error/(?P<radio_id>.*)$', 'collector.views.radioserver_error' ),
                       ( r'^radio_update/(?P<radio_id>.*)/(?P<device_id>.*)/(?P<latitude>.*)/(?P<longitude>.*)/$', 'collector.views.update_radio_positions' ),
                       ( r'^register_user/(?P<username>.*)/(?P<password>.*)/', 'collector.views.user_registration' ),
 )

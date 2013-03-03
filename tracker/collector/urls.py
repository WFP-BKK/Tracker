from django.conf.urls import  patterns


urlpatterns = patterns( 
                       '',
                       ( r'^requests.php', 'collector.views.collect' ),
                       ( r'^update/', 'collector.views.update_current' ),
                       ( r'^upload.php', 'collector.views.upload' ),
                       ( r'^export.php', 'collector.views.export' ),
                       ( r'^gm.php', 'mapper.views.gm' ),
 )

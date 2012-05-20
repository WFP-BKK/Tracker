from django.conf.urls.defaults import  patterns


urlpatterns = patterns( 
                       '',
                       ( r'^/all_items/$', 'kml.views.all_points' ),
                       ( r'^.kml$', 'kml.views.all_points_kml' ),
                       ( r'^.json$', 'kml.views.all_points_json' ),
                       ( r'^.rss$', 'kml.views.all_points_rss' ),
                       ( r'^/current.rss$', 'kml.views.all_points_rss' ),
                       ( r'^/paths.kml', 'kml.views.all_paths_kml' ),
                       ( r'^/path/(?P<user>.*).rss', 'kml.views.one_path_rss' ),                       
                       ( r'^/paths.rss', 'kml.views.all_paths_rss' ),
                       ( r'^/style.kml', 'kml.views.get_styles' ),
                       ( r'^/poi.kml', 'kml.views.show_poi' ),
                       ( r'^/poi.rss', 'kml.views.show_poi_rss' ),
                       ( r'^/images.rss', 'kml.views.show_images_rss' ),

 )

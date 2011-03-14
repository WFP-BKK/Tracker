from django.conf.urls.defaults import  patterns


urlpatterns = patterns(
                       '',
                       (r'^/all_items/$', 'kml.views.all_points'),
                       (r'^.kml$', 'kml.views.all_points_kml'),
                       (r'^/paths.kml','kml.views.all_paths_kml'),
)

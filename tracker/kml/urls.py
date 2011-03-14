from django.conf.urls.defaults import  patterns


urlpatterns = patterns(
                       '',
                       (r'^/all_items/$', 'tracker.kml.views.all_points'),
                       (r'^.kml$', 'tracker.kml.views.all_points_kml'),
                       (r'^/paths.kml','tracker.kml.views.all_paths_kml'),
)

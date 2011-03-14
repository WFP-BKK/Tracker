from django.conf.urls.defaults import  patterns


urlpatterns = patterns(
                       '',
                       (r'^requests.php', 'collector.views.collect'),
                       (r'^update$','collector.views.update_current')
)

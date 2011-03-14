from django.conf.urls.defaults import  patterns


urlpatterns = patterns(
                       '',
                       (r'^requests.php', 'tracker.collector.views.collect'),
                       (r'^update$','tracker.collector.views.update_current')
)

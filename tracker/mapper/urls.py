from django.conf.urls.defaults import patterns
from tracker import settings

urlpatterns = patterns(
                       '',
                       (r'^$', 'mapper.views.show_map'),
                       (r'^images/(?P<path>.*)$', 'django.views.static.serve',
                            {'document_root': settings.STATIC_DOC_ROOT}),
)

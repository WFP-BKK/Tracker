from django.conf.urls import patterns
from django.views.generic.base import TemplateView

urlpatterns = patterns( 
                       '',
                       ( r'^$', TemplateView.as_view(template_name='map.html') ),
                       ( r'^incidents$', TemplateView.as_view(template_name='incidents.html') ),
                       ( r'^upload$', TemplateView.as_view(template_name='upload.html') ),

 )

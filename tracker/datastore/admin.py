from django.contrib.gis import admin
from datastore.models import *



class CurrentPositionInline( admin.TabularInline ):
    model = CurrentPosition
class ActionUserAdmin( admin.ModelAdmin ):
    search_fields = ['username']
class PositionAdmin( admin.ModelAdmin ):
    model = Position

admin.site.register(Position)
admin.site.register( Icon )
admin.site.register( LoggingList )
admin.site.register( ActionUser, ActionUserAdmin )

admin.site.register(Incident, admin.OSMGeoAdmin)
admin.site.register(GeoFence, admin.OSMGeoAdmin)
admin.site.register(RadioServer)

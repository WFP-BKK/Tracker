from django.contrib.gis import admin
from datastore.models import *



class CurrentPositionInline( admin.TabularInline ):
    model = CurrentPosition
    
class ActionUserAdmin( admin.ModelAdmin ):
    search_fields = ['username']
    list_display = ('username','id')
    
class PositionAdmin( admin.ModelAdmin ):
    search_fields = ['user__username','user__firstName','user__lastName']
    model = Position
    list_display = ('user','location','dateoccurred')

class SeverAdmin(admin.ModelAdmin):
    model = RadioServer
    list_display = ('serverName', 'latestUpdate','latestCheck','refreshPeriod')

admin.site.register(Position,PositionAdmin)
admin.site.register( Icon )
admin.site.register( LoggingList )
admin.site.register( ActionUser, ActionUserAdmin )

admin.site.register(Incident, admin.OSMGeoAdmin)
admin.site.register(GeoFence, admin.OSMGeoAdmin)
admin.site.register(RadioServer,SeverAdmin)

from django.contrib.gis import admin
from datastore.models import *



class UserDetailInline( admin.StackedInline ):
    model = UserDetail
class CurrentPositionInline( admin.TabularInline ):
    model = CurrentPosition
class ActionUserAdmin( admin.ModelAdmin ):
    inlines = [
        UserDetailInline,# ContactWaysInline,#CurrentPositionInline
    ]
    search_fields = ['username']
class PositionAdmin( admin.ModelAdmin ):
    model = Position

admin.site.register(Position)
admin.site.register( Icon )
admin.site.register( ActionUser, ActionUserAdmin )
admin.site.register(Incident, admin.OSMGeoAdmin)
admin.site.register(GeoFence, admin.OSMGeoAdmin)
admin.site.register(RadioServer)
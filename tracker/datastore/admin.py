from django.contrib import admin
from datastore.models import UserDetail, ActionUser, Icon, CurrentPosition, Position



class UserDetailInline( admin.StackedInline ):
    model = UserDetail
class CurrentPositionInline( admin.TabularInline ):
    model = CurrentPosition
class ActionUserAdmin( admin.ModelAdmin ):
    inlines = [
        UserDetailInline, ContactWaysInline,#CurrentPositionInline
    ]
    search_fields = ['username']
class PositionAdmin( admin.ModelAdmin ):
    model = Position

admin.site.register(Position)
admin.site.register( Icon )
admin.site.register( ActionUser, ActionUserAdmin )

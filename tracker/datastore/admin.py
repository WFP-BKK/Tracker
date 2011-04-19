from django.contrib import admin
from datastore.models import UserDetail, ActionUser, Icon



class UserDetailInline( admin.StackedInline ):
    model = UserDetail

class ActionUserAdmin( admin.ModelAdmin ):
    inlines = [
        UserDetailInline,
    ]

admin.site.register( ActionUser, ActionUserAdmin )
admin.site.register( Icon )

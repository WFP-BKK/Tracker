from django.contrib import admin
from datastore.models import UserDetail, ActionUser, Icon, ContactWays



class UserDetailInline( admin.StackedInline ):
    model = UserDetail
class ContactWaysInline( admin.TabularInline ):
    model = ContactWays

class ActionUserAdmin( admin.ModelAdmin ):
    inlines = [
        UserDetailInline, ContactWaysInline,
    ]

admin.site.register( ActionUser, ActionUserAdmin )
admin.site.register( Icon )

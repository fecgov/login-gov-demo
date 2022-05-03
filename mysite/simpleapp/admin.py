from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from simpleapp.models import FECFileUser

# Define an inline admin descriptor for FECFileUserInline model
# which acts a bit like a singleton
# This allows us to see FECFile user fields in app admin
class FECFileUserInline(admin.StackedInline):
    model = FECFileUser
    can_delete = False
    verbose_name_plural = 'FECFileUser'

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (FECFileUserInline,)

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

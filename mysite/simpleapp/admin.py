from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class CustomUserAdmin(UserAdmin):
    fieldsets = (
        *UserAdmin.fieldsets,  # original form fieldsets, expanded
        (                      # new fieldset added on to the bottom
            'Login.gov information',  # group heading of your choice; set to None for a blank space instead of a header
            {
                'fields': (
                    'uuid',
                ),
            },
        ),
    )

admin.site.register(User, CustomUserAdmin)

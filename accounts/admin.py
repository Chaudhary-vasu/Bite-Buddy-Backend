from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    list_display = ('email', 'role')  # Add the fields you want to display
    ordering = ('email',)
    fieldsets = (
        (None, {'fields': ('email', 'password','role')}),
        # Add additional fields from your CustomUser model if needed
    )

admin.site.register(CustomUser, CustomUserAdmin)

from django.contrib import admin

from .models import (
    CustomUser,
    UserProfile,
)

admin.site.site.register(CustomUser)
admin.site.site.register(UserProfile)

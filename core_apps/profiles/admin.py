from django.contrib import admin
from .models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ["pkid", "user", "id", "gender", "phone_number", "country", "city"]
    list_display_links = ["pkid", "user"]
    list_filter = ["id", "pkid"]


admin.site.register(Profile, ProfileAdmin)

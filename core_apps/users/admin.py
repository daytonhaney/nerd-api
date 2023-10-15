from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

from .forms import UserCreationForm, UserChangeForm
from .models import User


class UserAdmin(BaseUserAdmin):
    ordering = ["email"]
    form = UserChangeForm
    add_form = UserCreationForm
    model = User

    list_display = [
        "id",
        "pkid",
        "email",
        "first_name",
        "last_name",
        "is_staff",
        "is_active",
    ]

    list_display_links = ["id", "pkid", "email"]

    list_filter = ["email", "is_staff", "is_active"]

    list_filters = (
        (_("Login Credentials"), {"fields": ("email", "password")}),
        (_("Personal Info"), {"fields": ("first_name", "last_name")}),
        (
            _("Permissions and Groups"),
            {
                "fields": (
                    "is_staff",
                    "is_active",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        (_("Important Dates"), {"fields": ("last_login", "date_joined", "last_name")}),
    )

    add_fieldsets = (
        None,
        {
            "classes": ("wide",),
            "fields": ("email", "first_name", "password1", "password2"),
        },
    )


admin.site.register(User, UserAdmin)

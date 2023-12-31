from django.contrib import admin
from django.contrib.auth.models import User, Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.admin import GroupAdmin as BaseGroupAdmin
from django.utils.translation import gettext_lazy as _

from auditlog.registry import auditlog
from auditlog.models import LogEntry
from auditlog.admin import LogEntryAdmin as BaseLogEntryAdmin
from unfold.admin import ModelAdmin
from unfold.forms import AdminPasswordChangeForm, UserChangeForm, UserCreationForm


class UserAdmin(BaseUserAdmin, ModelAdmin):
    """
    Override default forms with forms provided by Unfold admin, and hide password hash field.
    """

    fieldsets = (
        (None, {"fields": ["username"]}),
        (_("Personal info"), {"fields": ("first_name", "last_name", "email")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )

    form = UserChangeForm
    add_form = UserCreationForm
    change_password_form = AdminPasswordChangeForm


class GroupAdmin(BaseGroupAdmin, ModelAdmin):
    pass


class LogEntryAdmin(BaseLogEntryAdmin, ModelAdmin):
    pass


# Replace default User/Group and LogEntry admins with Unfold admin
admin.site.unregister(User)
admin.site.unregister(Group)
admin.site.unregister(LogEntry)
admin.site.register(User, UserAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(LogEntry, LogEntryAdmin)

admin.site.index_title = "Dashboard"  # Rename index to dashboard
admin.site.site_url = None  # Hide "visit site" link

# Register User and Group models with the auditlog app
auditlog.register(User)
auditlog.register(Group)

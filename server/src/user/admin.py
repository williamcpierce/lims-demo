from django.contrib import admin
from django.contrib.auth.models import User, Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.admin import GroupAdmin as BaseGroupAdmin

from auditlog.models import LogEntry
from auditlog.admin import LogEntryAdmin as BaseLogEntryAdmin
from unfold.admin import ModelAdmin
from unfold.forms import AdminPasswordChangeForm, UserChangeForm, UserCreationForm


class UserAdmin(BaseUserAdmin, ModelAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    change_password_form = AdminPasswordChangeForm


class GroupAdmin(BaseGroupAdmin, ModelAdmin):
    pass


class LogEntryAdmin(BaseLogEntryAdmin, ModelAdmin):
    pass


admin.site.unregister(User)
admin.site.unregister(Group)
admin.site.unregister(LogEntry)
admin.site.register(User, UserAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(LogEntry, LogEntryAdmin)

from django.contrib import admin
from django.db import models
from unfold.admin import ModelAdmin
from unfold.contrib.forms.widgets import WysiwygWidget

from .models import Entry
from .forms import EntryForm


class EntryAdmin(ModelAdmin):
    """
    Admin interface for the 'Entry' model.
    """

    form = EntryForm
    list_display = ["title", "author", "created_at", "updated_at"]
    readonly_fields = ("updated_at", "created_at", "author", "last_modified_by")

    formfield_overrides = {
        models.TextField: {
            "widget": WysiwygWidget,
        }
    }

    fieldsets = (
        (None, {"fields": ("title", "text")}),
        (
            "Authorship",
            {
                "fields": ("author", "created_at", "last_modified_by", "updated_at"),
            },
        ),
    )

    def save_model(self, request, obj, form, change):
        if obj.author == None:
            obj.author = request.user
        obj.last_modified_by = request.user
        obj.save()


admin.site.register(Entry, EntryAdmin)

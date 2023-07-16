from django.contrib import admin
from .models import Location, Container
from unfold.admin import ModelAdmin


class LocationAdmin(ModelAdmin):
    list_display = ["name", "parent", "hierarchy"]
    search_fields = ["name"]


class ContainerAdmin(ModelAdmin):
    list_display = ["barcode", "location", "_get_contents"]
    search_fields = ["barcode", "location"]
    filter_horizontal = ("contents",)

    def _get_contents(self, obj):
        return obj.get_contents()

    _get_contents.short_description = "Contents"


admin.site.register(Location, LocationAdmin)
admin.site.register(Container, ContainerAdmin)

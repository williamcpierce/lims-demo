from django.contrib import admin
from .models import Location
from unfold.admin import ModelAdmin


class LocationAdmin(ModelAdmin):
    list_display = ["name", "parent", "hierarchy"]
    search_fields = ["name"]


admin.site.register(Location, LocationAdmin)

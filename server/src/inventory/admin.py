from django.contrib import admin
from .models import Location, Container
from unfold.admin import ModelAdmin


class LocationAdmin(ModelAdmin):
    list_display = ["name", "parent", "hierarchy"]
    search_fields = ["name"]


class ContainerAdmin(ModelAdmin):
    list_display = ["barcode", "location"]
    search_fields = ["barcode", "location"]


admin.site.register(Location, LocationAdmin)
admin.site.register(Container, ContainerAdmin)

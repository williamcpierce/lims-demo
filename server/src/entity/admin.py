from django.contrib import admin
from .models import Type, Sample
from unfold.admin import ModelAdmin


class TypeAdmin(ModelAdmin):
    list_display = ["name", "prefix"]
    search_fields = ["name", "prefix"]


class SampleAdmin(ModelAdmin):
    list_display = ["type", "__str__", "_get_containers"]
    search_fields = ["type", "__str__"]
    filter_horizontal = ("containers",)
    readonly_fields = ["containers"]

    def _get_containers(self, obj):
        return obj.get_containers()

    _get_containers.short_description = "Containers"


admin.site.register(Type, TypeAdmin)
admin.site.register(Sample, SampleAdmin)

from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from unfold.admin import ModelAdmin
from unfold.contrib.import_export.forms import ExportForm, ImportForm

from .models import Container, Location


class LocationAdmin(ModelAdmin, ImportExportModelAdmin):
    list_display = ["name", "parent", "hierarchy"]
    search_fields = ["name"]
    import_form_class = ImportForm
    export_form_class = ExportForm


class ContainerAdmin(ModelAdmin, ImportExportModelAdmin):
    list_display = ["barcode", "location", "_get_contents"]
    search_fields = ["barcode", "location"]
    filter_horizontal = ("contents",)
    import_form_class = ImportForm
    export_form_class = ExportForm

    def _get_contents(self, obj):
        return obj.get_contents()

    _get_contents.short_description = "Contents"


admin.site.register(Location, LocationAdmin)
admin.site.register(Container, ContainerAdmin)

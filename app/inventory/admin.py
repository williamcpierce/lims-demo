from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from unfold.admin import ModelAdmin
from unfold.contrib.import_export.forms import ExportForm, ImportForm

from .models import Container, Location
from .resources import ContainerResource


class LocationAdmin(ModelAdmin):
    """
    Admin interface for the 'Location' model.
    """

    list_display = ["name", "parent", "hierarchy"]
    search_fields = ["name"]


class ContainerAdmin(ModelAdmin, ImportExportModelAdmin):
    """
    Admin interface for the 'Container' model with import/export functionality.
    """

    list_display = ["barcode", "location", "_get_contents"]
    search_fields = ["barcode"]

    filter_horizontal = (
        "contents",
    )  # Display contents field using horizontal filter widget

    resource_classes = [ContainerResource]
    import_form_class = ImportForm
    export_form_class = ExportForm

    def _get_contents(self, obj):  # Allows display and naming of class method
        return obj.get_contents()

    _get_contents.short_description = "Contents"


admin.site.register(Location, LocationAdmin)
admin.site.register(Container, ContainerAdmin)

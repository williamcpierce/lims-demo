from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export.widgets import ForeignKeyWidget
from unfold.admin import ModelAdmin
from unfold.contrib.import_export.forms import ExportForm, ImportForm

from .models import Sample, Type, Field
from .resources import SampleResource


class TypeAdmin(ModelAdmin):
    """
    Admin interface for the 'Type' model.
    """

    list_display = ["name", "prefix", "_get_fields"]
    search_fields = ["name", "prefix"]

    filter_horizontal = (
        "fields",
    )  # Display contents field using horizontal filter widget

    def _get_fields(self, obj):  # Allows display and naming of class method
        return obj.get_fields()

    _get_fields.short_description = "Fields"


class FieldAdmin(ModelAdmin):
    """
    Admin interface for the 'Field' model.
    """

    def has_module_permission(self, request):
        """
        Hides field admin page from admin index.
        """
        return False


class SampleAdmin(ModelAdmin, ImportExportModelAdmin):
    """
    Admin interface for the 'Sample' model with import/export functionality.
    """

    list_display = ["name", "alias", "_get_containers"]
    list_filter = ["type"]
    readonly_fields = ["name", "containers"]
    search_fields = ["name", "alias"]

    filter_horizontal = ("containers",)

    resource_classes = [SampleResource]
    import_form_class = ImportForm
    export_form_class = ExportForm

    def get_fields(self, request, obj=None):
        """
        Overrides the default get_fields method for generating forms,
        to enable dynamic fields defined by sample type
        """
        base_fields = ("name", "type")
        if obj == None:
            return base_fields
        sample_type = getattr(obj, "type")
        additional_fields = (str(c) for c in getattr(sample_type, "fields").all())
        return base_fields + tuple(additional_fields)

    def _get_containers(self, obj):  # Allows display and naming of class method
        return obj.get_containers()

    _get_containers.short_description = "Containers"


admin.site.register(Type, TypeAdmin)
admin.site.register(Sample, SampleAdmin)
admin.site.register(Field, FieldAdmin)

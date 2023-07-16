from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from unfold.admin import ModelAdmin
from unfold.contrib.import_export.forms import ExportForm, ImportForm

from .models import Sample, Schema


class SchemaAdmin(ModelAdmin):
    list_display = ["name", "prefix"]
    search_fields = ["name", "prefix"]


class SampleAdmin(ModelAdmin, ImportExportModelAdmin):
    list_display = ["name", "schema", "_get_containers"]
    search_fields = ["name", "schema"]
    filter_horizontal = ("containers",)
    readonly_fields = ["containers"]
    import_form_class = ImportForm
    export_form_class = ExportForm

    def _get_containers(self, obj):
        return obj.get_containers()

    _get_containers.short_description = "Containers"


admin.site.register(Schema, SchemaAdmin)
admin.site.register(Sample, SampleAdmin)

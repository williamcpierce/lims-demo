from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export.widgets import ForeignKeyWidget
from unfold.admin import ModelAdmin
from unfold.contrib.import_export.forms import ExportForm, ImportForm

from .models import Sample, Type
from .resources import SampleResource


class TypeAdmin(ModelAdmin):
    list_display = ["name", "prefix", "digits"]
    search_fields = ["name", "prefix"]


class SampleAdmin(ModelAdmin, ImportExportModelAdmin):
    fields = ("name", "type", "alias" "containers")
    list_display = ["name", "alias", "_get_containers"]
    list_filter = ["type"]
    readonly_fields = ["name", "containers"]
    search_fields = ["name", "alias"]

    filter_horizontal = ("containers",)

    resource_classes = [SampleResource]
    import_form_class = ImportForm
    export_form_class = ExportForm

    def _get_containers(self, obj):
        return obj.get_containers()

    _get_containers.short_description = "Containers"


admin.site.register(Type, TypeAdmin)
admin.site.register(Sample, SampleAdmin)

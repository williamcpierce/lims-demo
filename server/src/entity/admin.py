from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from unfold.admin import ModelAdmin
from unfold.contrib.import_export.forms import ExportForm, ImportForm

from .models import Sample, Type


class TypeAdmin(ModelAdmin, ImportExportModelAdmin):
    list_display = ["name", "prefix"]
    search_fields = ["name", "prefix"]
    import_form_class = ImportForm
    export_form_class = ExportForm


class SampleAdmin(ModelAdmin, ImportExportModelAdmin):
    list_display = ["type", "__str__", "_get_containers"]
    search_fields = ["type", "__str__"]
    filter_horizontal = ("containers",)
    readonly_fields = ["containers"]
    import_form_class = ImportForm
    export_form_class = ExportForm

    def _get_containers(self, obj):
        return obj.get_containers()

    _get_containers.short_description = "Containers"


admin.site.register(Type, TypeAdmin)
admin.site.register(Sample, SampleAdmin)

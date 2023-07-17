from import_export import fields, resources
from import_export.widgets import ForeignKeyWidget

from .models import Sample, Type


class SampleResource(resources.ModelResource):
    type = fields.Field(
        column_name="type",
        attribute="type",
        widget=ForeignKeyWidget(Type, field="prefix"),
    )

    class Meta:
        model = Sample
        fields = ("id", "type", "alias")

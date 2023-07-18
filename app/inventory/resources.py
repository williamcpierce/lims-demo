from import_export import fields, resources
from import_export.widgets import ForeignKeyWidget, ManyToManyWidget

from .models import Container, Location
from registry.models import Sample


class ContainerResource(resources.ModelResource):
    location = fields.Field(
        column_name="location",
        attribute="location",
        widget=ForeignKeyWidget(Location, field="prefix"),
    )

    contents = fields.Field(
        column_name="contents",
        attribute="contents",
        widget=ManyToManyWidget(Sample, field="name"),
    )

    class Meta:
        model = Container
        fields = ("id", "barcode", "location", "contents")

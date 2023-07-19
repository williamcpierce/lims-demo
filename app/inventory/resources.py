from import_export import fields, resources
from import_export.widgets import ForeignKeyWidget, ManyToManyWidget

from .models import Container, Location
from registry.models import Sample


class ContainerResource(resources.ModelResource):
    """
    Resource class for importing and exporting 'Container' model data.
    """

    # Import and export Location references by name instead of pk
    location = fields.Field(
        column_name="location",
        attribute="location",
        widget=ForeignKeyWidget(Location, field="name"),
    )

    # Import and export Sample references by name instead of pk
    contents = fields.Field(
        column_name="contents",
        attribute="contents",
        widget=ManyToManyWidget(Sample, field="name"),
    )

    class Meta:
        model = Container
        fields = ("id", "barcode", "location", "contents")

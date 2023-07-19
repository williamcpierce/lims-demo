from import_export import fields, resources
from import_export.widgets import ForeignKeyWidget

from .models import Sample, Type


class SampleResource(resources.ModelResource):
    """
    Resource class for importing and exporting 'Sample' model data.
    """

    # Import and export Type references by prefix instead of pk
    type = fields.Field(
        column_name="type",
        attribute="type",
        widget=ForeignKeyWidget(Type, field="prefix"),
    )

    # Import and export Sample references by name instead of pk
    related = fields.Field(
        column_name="related",
        attribute="related",
        widget=ForeignKeyWidget(Sample, field="name"),
    )

    class Meta:
        model = Sample
        fields = ("id", "type", "alias", "name", "related", "sequence")

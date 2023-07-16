from django.db import models
from mptt.models import MPTTModel


class Location(MPTTModel):
    name = models.CharField(max_length=50, unique=False)
    parent = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="children",
    )

    @property
    def hierarchy(self):
        ancestors = [x.name for x in self.get_ancestors(include_self=True)]
        return " > ".join(ancestors)

    def __str__(self):
        return self.hierarchy

    class MPTTMeta:
        order_insertion_by = ["name"]


class Container(models.Model):
    barcode = models.CharField(max_length=50, unique=True)
    location = models.ForeignKey(
        Location,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    contents = models.ManyToManyField("entity.Sample", blank=True)

    def __str__(self):
        return self.barcode

    def get_contents(self):
        return ", ".join([str(c) for c in self.contents.all()])

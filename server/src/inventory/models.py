from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Location(MPTTModel):
    name = models.CharField(max_length=50, unique=True)
    parent = TreeForeignKey(
        "self", on_delete=models.CASCADE, null=True, blank=True, related_name="children"
    )

    def hierarchy(self):
        ancestors = [x.name for x in self.get_ancestors(include_self=True)]
        return ":".join(ancestors)

    def __str__(self):
        return self.name

    class MPTTMeta:
        order_insertion_by = ["name"]

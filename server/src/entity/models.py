from django.db import models
from inventory.models import Container


class Type(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    prefix = models.CharField(max_length=3, unique=True)
    digits = models.IntegerField()

    def __str__(self):
        return self.prefix


class Sample(models.Model):
    _id = models.IntegerField(
        verbose_name="ID",
        null=True,
        blank=True,
    )
    type = models.ForeignKey(
        Type,
        on_delete=models.CASCADE,
        null=False,
        blank=True,
    )
    containers = models.ManyToManyField(
        Container,
        through=Container.contents.through,
        blank=True,
    )

    def __str__(self):
        padded_id = str(self._id).rjust(self.type.digits, "0")
        return f"{self.type.prefix}{padded_id}"

    def get_containers(self):
        return ", ".join([str(c) for c in self.containers.all()])

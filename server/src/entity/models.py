from django.db import models
from inventory.models import Container


class Schema(models.Model):
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
    schema = models.ForeignKey(
        Schema,
        on_delete=models.CASCADE,
        null=False,
        blank=True,
    )
    containers = models.ManyToManyField(
        Container,
        through=Container.contents.through,
        blank=True,
    )
    name = models.CharField(
        max_length=50,
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        padded_id = str(self._id).rjust(self.type.digits, "0")
        self.name = f"{self.type.prefix}{padded_id}"
        super(Sample, self).save(*args, **kwargs)

    def get_containers(self):
        return ", ".join([str(c) for c in self.containers.all()])

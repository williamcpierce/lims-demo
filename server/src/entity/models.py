from auditlog.registry import auditlog
from django.db import models
from inventory.models import Container


class Schema(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    prefix = models.CharField(max_length=3, unique=True)
    digits = models.IntegerField(verbose_name="ID Digits")

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
        return self.generate_name()

    def generate_name(self):
        padded_id = str(self._id).rjust(self.schema.digits, "0")
        return f"{self.schema.prefix}{padded_id}"

    def save(self, *args, **kwargs):
        self.name = self.generate_name()
        super(Sample, self).save(*args, **kwargs)

    def get_containers(self):
        return ", ".join([str(c) for c in self.containers.all()])


auditlog.register(Schema)
auditlog.register(Sample)

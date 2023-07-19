from auditlog.registry import auditlog
from django.db import models
from inventory.models import Container


class Type(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    prefix = models.CharField(max_length=3, unique=True)
    fields = models.ManyToManyField("Field", blank=True)

    def __str__(self):
        return self.prefix

    def get_fields(self):
        return ", ".join([str(c) for c in self.fields.all()])


class Field(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Sample(models.Model):
    alias = models.CharField(
        max_length=100,
        blank=True,
        null=True,
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
    name = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name="ID",
    )
    related = models.ForeignKey(
        "Sample",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="related_sample",
    )
    sequence = models.TextField(
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.generate_name()

    def generate_name(self):
        padded_id = str(self.id).rjust(3, "0")
        return f"{self.type.prefix}{padded_id}"

    def save(self, *args, **kwargs):
        """
        Overrides the default model save behavior, so that a custom name
        can be generated which includes the PK (which is only available
        after the first save operation).
        """
        super(Sample, self).save(*args, **kwargs)
        self.name = self.generate_name()
        super(Sample, self).save(*args, **kwargs)

    def get_containers(self):
        return ", ".join([str(c) for c in self.containers.all()])


# Register Type, Sample, and Field models with the auditlog app
auditlog.register(Type)
auditlog.register(Sample)
auditlog.register(Field)

from django.contrib.auth.models import User
from auditlog.registry import auditlog
from django.db import models


class Entry(models.Model):
    title = models.CharField(
        max_length=100,
        blank=False,
        null=True,
    )
    text = models.TextField(
        null=True,
        blank=True,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        null=True,
        blank=True,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        null=True,
        blank=True,
        verbose_name="Last modified at",
    )
    author = models.ForeignKey(
        User,
        null=True,
        on_delete=models.SET_NULL,
        related_name="entries",
    )
    last_modified_by = models.ForeignKey(
        User,
        related_name="entry_modifier",
        blank=True,
        on_delete=models.SET_NULL,
        null=True,
    )

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name_plural = "Entries"


# Register Entry model with the auditlog app
auditlog.register(Entry)

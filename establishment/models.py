from django.db import models
from config.models import TimestampedModel


class Establishment(TimestampedModel):
    name = models.CharField("Name", max_length=255)
    description = models.TextField("Description")
    location = models.CharField("Location", max_length=255)
    opening_hours = models.IntegerField("Opening Hours")
    # open_time = models.DateTimeField("Opening Time")
    # close_time = models.DateTimeField("Close Time")

    class Meta:
        verbose_name = "Establishment"
        verbose_name_plural = "Establishments"
        ordering = ("-created_at",)

    def __str__(self):
        return self.name

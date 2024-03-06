from django.db import models
from config.models import TimestampedModel


class Product(TimestampedModel):
    name = models.CharField("Name", max_length=255)
    description = models.TextField("Description")
    price = models.PositiveIntegerField("Price", default=0)
    quantity = models.PositiveIntegerField("Quantity", default=0)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ("-created_at",)

    def __str__(self):
        return self.name


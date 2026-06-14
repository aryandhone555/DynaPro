from django.db import models


class Resource(models.Model):

    RESOURCE_TYPES = [
        ("APP", "Application"),
        ("DB", "Database"),
    ]

    ENVIRONMENTS = [
        ("PROD", "Production"),
        ("UAT", "UAT"),
        ("DEV", "Development"),
    ]

    name = models.CharField(max_length=100, unique=True)

    resource_type = models.CharField(
        max_length=10,
        choices=RESOURCE_TYPES
    )

    environment = models.CharField(
        max_length=10,
        choices=ENVIRONMENTS,
        default="PROD"
    )

    is_active = models.BooleanField(default=True)

    description = models.TextField(
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return f"{self.name} ({self.resource_type})"
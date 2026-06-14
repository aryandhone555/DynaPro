from django.db import models
from resources.models import Resource


    
class MetricDefinition(models.Model):

    RESOURCE_TYPES = [
        ("APP", "Application"),
        ("DB", "Database"),
    ]

    name = models.CharField(max_length=100)

    resource_type = models.CharField(
        max_length=10,
        choices=RESOURCE_TYPES
    )

    unit = models.CharField(max_length=20)

    warning_threshold = models.FloatField(
        null=True,
        blank=True
    )

    critical_threshold = models.FloatField(
        null=True,
        blank=True
    )

    description = models.TextField(
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        unique_together = (
            "name",
            "resource_type",
        )

    def __str__(self):
        return self.name
    

class MetricData(models.Model):

    STATUS_CHOICES = [
        ("GREEN", "GREEN"),
        ("AMBER", "AMBER"),
        ("RED", "RED"),
    ]

    resource = models.ForeignKey(
        Resource,
        on_delete=models.CASCADE
    )

    metric = models.ForeignKey(
        MetricDefinition,
        on_delete=models.CASCADE
    )

    value = models.FloatField()

    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES
    )

    timestamp = models.DateTimeField(
        db_index=True
    )

    class Meta:

        indexes = [

            models.Index(
                fields=[
                    "resource",
                    "metric",
                    "-timestamp"
                ]
            ),

            models.Index(
                fields=["timestamp"]
            ),
        ]

        ordering = ["-timestamp"]

    def __str__(self):
        return (
            f"{self.resource.name} - "
            f"{self.metric.name}"
        )
from django.core.management.base import BaseCommand
from metrics.models import MetricDefinition


class Command(BaseCommand):

    help = "Seed metric definitions"

    def handle(self, *args, **kwargs):

        metrics = [

            # APP Metrics
            {
                "name": "CPU Usage",
                "resource_type": "APP",
                "unit": "%",
                "warning_threshold": 70,
                "critical_threshold": 90,
            },
            {
                "name": "Memory Usage",
                "resource_type": "APP",
                "unit": "%",
                "warning_threshold": 75,
                "critical_threshold": 90,
            },
            {
                "name": "Response Time",
                "resource_type": "APP",
                "unit": "ms",
                "warning_threshold": 300,
                "critical_threshold": 1000,
            },
            {
                "name": "Request Rate",
                "resource_type": "APP",
                "unit": "req/s",
                "warning_threshold": None,
                "critical_threshold": None,
            },
            {
                "name": "Error Rate",
                "resource_type": "APP",
                "unit": "%",
                "warning_threshold": 2,
                "critical_threshold": 5,
            },
            {
                "name": "Availability",
                "resource_type": "APP",
                "unit": "%",
                "warning_threshold": 99.5,
                "critical_threshold": 98,
            },

            # DB Metrics
            {
                "name": "CPU Usage",
                "resource_type": "DB",
                "unit": "%",
                "warning_threshold": 75,
                "critical_threshold": 90,
            },
            {
                "name": "Memory Usage",
                "resource_type": "DB",
                "unit": "%",
                "warning_threshold": 80,
                "critical_threshold": 95,
            },
            {
                "name": "Connections",
                "resource_type": "DB",
                "unit": "count",
                "warning_threshold": 800,
                "critical_threshold": 1000,
            },
            {
                "name": "Query Latency",
                "resource_type": "DB",
                "unit": "ms",
                "warning_threshold": 100,
                "critical_threshold": 500,
            },
            {
                "name": "Disk Usage",
                "resource_type": "DB",
                "unit": "%",
                "warning_threshold": 80,
                "critical_threshold": 95,
            },
            {
                "name": "TPS",
                "resource_type": "DB",
                "unit": "tx/s",
                "warning_threshold": None,
                "critical_threshold": None,
            },
        ]

        for metric in metrics:

            MetricDefinition.objects.get_or_create(
                name=metric["name"],
                resource_type=metric["resource_type"],
                defaults=metric
            )

        self.stdout.write(
            self.style.SUCCESS(
                "Metrics seeded successfully"
            )
        )